import json
d = json.load(open('catdiff.json', encoding='utf-8'))
q = lambda s: "'" + str(s).replace("'", "''") + "'"

p = d['pt']
patches = ',\n'.join(f"({pt},{leg},{qi},{q(field)},{q(new)})" for pt, leg, qi, field, new, old in p['patches'])
md5s = ','.join(f"({pt},{q(m)})" for pt, m in p['new_md5'].items())
pt_sql = f"""do $seed$
declare r record; b jsonb; n int;
begin
  for r in select pt, blueprint from public.timed_content_manifests_v1 where manifest_sha256 = {q(p['old'])} order by pt loop
    b := r.blueprint;
    for n in 1..1 loop null; end loop;
    select coalesce((select b2 from (select b as b2) x), b) into b;
    for r2 in select * from (values
{patches}
    ) v(pt, leg, qi, field, val) where v.pt = r.pt loop
      b := jsonb_set(b, array['legs', r2.leg::text, 'questions', r2.qi::text, r2.field], to_jsonb(r2.val), false);
    end loop;
    insert into public.timed_content_manifests_v1(manifest_sha256, pt, blueprint) values ({q(p['new'])}, r.pt, b) on conflict (manifest_sha256, pt) do nothing;
  end loop;
  select count(*) into n from public.timed_content_manifests_v1 t join (values {md5s}) e(pt, m) on t.pt = e.pt
    where t.manifest_sha256 = {q(p['new'])} and md5(t.blueprint::text) = e.m;
  if n <> 59 or (select count(*) from public.timed_content_manifests_v1 where manifest_sha256 = {q(p['new'])}) <> 59 then
    raise exception 'new PT catalog verification failed: % of 59 match', n;
  end if;
end $seed$;"""
# plpgsql needs r2 declared
pt_sql = pt_sql.replace("declare r record; b jsonb; n int;", "declare r record; r2 record; b jsonb; n int;")
pt_sql = pt_sql.replace("    for n in 1..1 loop null; end loop;\n    select coalesce((select b2 from (select b as b2) x), b) into b;\n", "")
open('seed_pt.sql', 'w', encoding='utf-8').write(pt_sql)

s = d['sec']
patches = ',\n'.join(f"({pt},{q(kind)},{sec},{qi},{q(field)},{q(new)})" for pt, kind, sec, qi, field, new, old in s['patches'])
md5s = ','.join("({},{},{},{})".format(k.split('|')[0], q(k.split('|')[1]), k.split('|')[2], q(m)) for k, m in s['new_md5'].items())
sec_sql = f"""do $seed$
declare r record; r2 record; b jsonb; n int;
begin
  for r in select pt, kind, section, definition from public.timed_section_content_manifests_v1 where manifest_sha256 = {q(s['old'])} order by pt, section loop
    b := r.definition;
    for r2 in select * from (values
{patches}
    ) v(pt, kind, section, qi, field, val) where v.pt = r.pt and v.kind = r.kind and v.section = r.section loop
      b := jsonb_set(b, array['questions', r2.qi::text, r2.field], to_jsonb(r2.val), false);
    end loop;
    insert into public.timed_section_content_manifests_v1(manifest_sha256, pt, kind, section, definition) values ({q(s['new'])}, r.pt, r.kind, r.section, b) on conflict do nothing;
  end loop;
  select count(*) into n from public.timed_section_content_manifests_v1 t join (values {md5s}) e(pt, kind, section, m) on t.pt = e.pt and t.kind = e.kind and t.section = e.section
    where t.manifest_sha256 = {q(s['new'])} and md5(t.definition::text) = e.m;
  if n <> 236 or (select count(*) from public.timed_section_content_manifests_v1 where manifest_sha256 = {q(s['new'])}) <> 236 then
    raise exception 'new section catalog verification failed: % of 236 match', n;
  end if;
end $seed$;"""
open('seed_sec.sql', 'w', encoding='utf-8').write(sec_sql)
print(len(pt_sql), len(sec_sql))
