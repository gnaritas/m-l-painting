# DEPLOY — M & L Painting (cohort B, 2026-11-19)
- Live preview: https://m-l-painting-demo.up.railway.app (custom domain via `railway domain update`)
- Repo: github.com/gnaritas/m-l-painting (generator build_site.py -> public/)
- Deploy: `railway up -s m-l-painting` from ~/sites/m-l-painting; workspace "Ramon Leon's Projects"; project/service ids via `railway status`
- Env: BREVO_API_KEY set (form relay -> jarvis+websites@onsmalltalk.com)
- Identity: stencil/signal-yellow on petrol ink. Verified facts only (NAP 3x: (360) 798-2333, 16012 NE 26th St, Vancouver WA 98684; no license claimed)
- Verification: _verify.py PASS 0 fails 0 warns; POST /contact -> 303 /thanks; og.png + style.css md5 live==local
