/* Original LSAT U study sculpture. Canvas is decorative; the page owns its semantics. */
(() => {
  const canvas = document.getElementById('logic-sculpture');
  if (!canvas) return;
  const context = canvas.getContext('2d', { alpha: true });
  if (!context) return;
  const stage = canvas.closest('.sculpture-stage') || canvas.parentElement;
  // Subpixel reconstruction softens painter-mesh seams without blurring page text.
  canvas.style.filter = 'blur(0.55px)';
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const TAU = Math.PI * 2;
  const rings = 240;
  const sides = 56;
  const mesh = [];
  let width = 0;
  let height = 0;
  let frame = 0;
  let start = 0;
  let settled = motion.matches;
  let visible = true;

  const normalize = v => {
    const length = Math.hypot(...v);
    return v.map(n => n / length);
  };
  const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
  const center = t => {
    const radius = 1.12 + 0.39 * Math.cos(3 * t);
    return [radius * Math.cos(2 * t), radius * Math.sin(2 * t), 0.58 * Math.sin(3 * t)];
  };

  // A continuous (2,3) torus knot with a softly flattened, twisting metallic tube.
  for (let i = 0; i < rings; i++) {
    const t = (i / rings) * TAU;
    const c = center(t);
    const next = center(t + 0.001);
    const tangent = normalize(next.map((v, axis) => v - c[axis]));
    const n = normalize(cross(tangent, [0, 0, 1]));
    const b = cross(tangent, n);
    const ring = [];
    for (let j = 0; j < sides; j++) {
      const a = (j / sides) * TAU;
      const twist = 0.35 * Math.sin(3 * t);
      const u = Math.cos(a + twist);
      const v = Math.sin(a + twist);
      const normal = normalize(n.map((value, axis) => value * u / 0.29 + b[axis] * v / 0.23));
      ring.push({ p: c.map((value, axis) => value + n[axis] * u * 0.29 + b[axis] * v * 0.23), n: normal, t });
    }
    mesh.push(ring);
  }

  function rotate(v, turn) {
    const z = -0.28;
    const y = 0.52 + turn;
    const x = 0.48;
    const a = v[0] * Math.cos(z) - v[1] * Math.sin(z);
    const b = v[0] * Math.sin(z) + v[1] * Math.cos(z);
    const c = a * Math.cos(y) + v[2] * Math.sin(y);
    const d = -a * Math.sin(y) + v[2] * Math.cos(y);
    return [c, b * Math.cos(x) - d * Math.sin(x), b * Math.sin(x) + d * Math.cos(x)];
  }

  const key = normalize([-0.65, -0.8, 1.4]);
  const half = normalize([key[0], key[1], key[2] + 1]);
  const dot = (a, b) => a.reduce((sum, value, index) => sum + value * b[index], 0);
  const clamp = value => Math.min(255, Math.max(0, Math.round(value)));

  function paint(turn = 0, step = 1) {
    if (!width || !height) return;
    context.clearRect(0, 0, width, height);
    const scale = Math.min(width / 3.7, height / 3.8);
    const cx = width * 0.5;
    const cy = height * 0.47;
    const shadow = context.createRadialGradient(cx, height * 0.87, 0, cx, height * 0.87, width * 0.3);
    shadow.addColorStop(0, 'rgba(0,0,0,.28)');
    shadow.addColorStop(1, 'rgba(0,0,0,0)');
    context.save();
    context.translate(0, height * 0.87);
    context.scale(1, 0.16);
    context.translate(0, -height * 0.87);
    context.fillStyle = shadow;
    context.fillRect(0, -height * 4, width, height * 10);
    context.restore();

    const vertices = mesh.map(ring => ring.map(vertex => {
      const p = rotate(vertex.p, turn);
      const n = rotate(vertex.n, turn);
      const perspective = 6.5 / (6.5 - p[2]);
      return { x: cx + p[0] * scale * perspective, y: cy + p[1] * scale * perspective, z: p[2], n, t: vertex.t };
    }));
    const faces = [];
    for (let i = 0; i < rings; i += step) {
      for (let j = 0; j < sides; j++) {
        const points = [vertices[i][j], vertices[(i + step) % rings][j], vertices[(i + step) % rings][(j + 1) % sides], vertices[i][(j + 1) % sides]];
        const n = normalize([0, 1, 2].map(axis => points.reduce((sum, point) => sum + point.n[axis], 0)));
        if (n[2] < -0.28) continue;
        faces.push({ points, n, depth: points.reduce((sum, point) => sum + point.z, 0) / 4 });
      }
    }
    faces.sort((a, b) => a.depth - b.depth);
    for (const face of faces) {
      const n = face.n;
      const diffuse = Math.max(0, dot(n, key));
      const specular = Math.pow(Math.max(0, dot(n, half)), 18);
      const broad = Math.pow(Math.max(0, dot(n, half)), 4);
      const rim = Math.pow(1 - Math.max(0, n[2]), 3);
      const warmth = (Math.sin(face.points[0].t * 3 + 0.7) + 1) / 2;
      // Colored bounce light keeps the unlit porcelain coral, rather than muddy brown.
      const shadowTone = [190, 88, 76];
      const litTone = [255, 229 + warmth * 6, 212 + warmth * 7];
      const light = 0.35 + diffuse * 0.65;
      const color = litTone.map((value, channel) => clamp(
        shadowTone[channel] + (value - shadowTone[channel]) * light
        + specular * 27 + broad * 9 + rim * [12, 10, 8][channel]
      ));
      context.fillStyle = `rgb(${color.join(',')})`;
      context.strokeStyle = context.fillStyle;
      context.lineWidth = 0.9;
      context.beginPath();
      face.points.forEach((point, index) => index ? context.lineTo(point.x, point.y) : context.moveTo(point.x, point.y));
      context.closePath();
      context.fill();
      context.stroke();
    }
  }

  function animate(time) {
    frame = 0;
    if (!visible || document.hidden) return;
    if (!start) start = time;
    const progress = Math.min(1, (time - start) / 1150);
    const ease = 1 - Math.pow(1 - progress, 3);
    paint(-0.36 * (1 - ease), 2);
    if (progress < 1 && !motion.matches) frame = requestAnimationFrame(animate);
    else { settled = true; paint(); }
  }

  function resize() {
    const bounds = stage.getBoundingClientRect();
    if (width === bounds.width && height === (bounds.height || 310)) return;
    width = bounds.width;
    height = bounds.height || 310;
    const ratio = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(width * ratio);
    canvas.height = Math.round(height * ratio);
    canvas.style.width = `${width}px`;
    canvas.style.height = `${height}px`;
    context.setTransform(ratio, 0, 0, ratio, 0, 0);
    paint();
  }
  new ResizeObserver(resize).observe(stage);
  new IntersectionObserver(entries => {
    visible = entries[0].isIntersecting;
    if (!visible) { cancelAnimationFrame(frame); frame = 0; }
    else if (!settled && !frame) frame = requestAnimationFrame(animate);
  }).observe(canvas);
  motion.addEventListener('change', () => {
    if (motion.matches) { cancelAnimationFrame(frame); frame = 0; settled = true; paint(); }
  });
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) { cancelAnimationFrame(frame); frame = 0; }
    else if (visible && !settled && !frame) frame = requestAnimationFrame(animate);
  });
  resize();
})();
