#!/usr/bin/env ruby
# Adds the neutral brain pointer to agent globals and deduplicates Codex project scopes.

kind, path = ARGV
abort "usage: align-runtime-file.rb KIND FILE" unless kind && path
text = File.binread(path)

case kind
when "claude"
  text = text.gsub("~/ai-os/wiki/synthesis/", "~/ai-os/wiki/domains/lsat-u/synthesis/")
  unless text.include?("# Unified brain OS")
    text << "\n# Unified brain OS\nThe canonical personal operating root is `~/ai-os`. Read `~/ai-os/CLAUDE.md` and `~/ai-os/system/schema/core.md`; use old gathered locations only as frozen sources.\n"
  end
when "codex-agents"
  unless text.include?("# Unified brain OS")
    text << "\n# Unified brain OS\nThe canonical personal operating root is `~/ai-os`. Read `~/ai-os/AGENTS.md` and `~/ai-os/system/schema/core.md`; use old gathered locations only as frozen sources.\n"
  end
when "codex-config"
  lines = text.lines
  output = []
  seen_brain = false
  skipping_duplicate = false
  lines.each do |line|
    if line.match?(/^\[projects\."\/Users\/joshuaf\/brain"\]\s*$/)
      if seen_brain
        skipping_duplicate = true
        next
      end
      seen_brain = true
      skipping_duplicate = false
      output << line
      next
    end
    if line.start_with?("[")
      skipping_duplicate = false
    end
    output << line unless skipping_duplicate
  end
  text = output.join
else
  abort "unknown alignment kind: #{kind}"
end

stat = File.stat(path)
tmp = "#{path}.brain-align-#{Process.pid}"
File.open(tmp, File::WRONLY | File::CREAT | File::EXCL, stat.mode & 0o7777) do |file|
  file.write(text)
  file.flush
  file.fsync
end
File.rename(tmp, path)
