#!/usr/bin/env python3
"""M & L Painting — template-v2 T2 site generator (2026-11-19, cohort B).
Identity: 'stencil & signal' — petrol ink on bone, signal-yellow tabs, tape
stripes, condensed uppercase display. Zero third-party JS.
Verified facts (card t_d5622672 + registry queue row): painters, Vancouver WA.
NAP 3x-confirmed: (360) 798-2333, 16012 NE 26th St 98684. GBP 5.0. Office
hours Mon–Fri 9–5 (Yahoo). Email mlpainting77@gmail.com on FB intro."""
import json, os

SLUG   = "m-l-painting"
ORIGIN = "https://m-l-painting-demo.up.railway.app"
SITE   = "M & L Painting"
BRAND  = "M &amp; L Painting"
PHONE  = "(360) 798-2333"
TEL    = "tel:+13607982333"
EMAIL  = "mlpainting77@gmail.com"
STREET = "16012 NE 26th St"
CITY, ST, ZIP = "Vancouver", "WA", "98684"
CITY_FULL = "Vancouver, Washington"
FB = "https://www.facebook.com/mlpaintingservice"
MAPQ = "https://www.google.com/maps?q=16012+NE+26th+St,+Vancouver,+WA+98684&amp;output=embed"
BUILT = "<!-- BUILT-2026-11-19 -->\n"

def head(title, desc, path, util=False):
    url = ORIGIN + ("/" if path == "/" else path)
    h = ['<!DOCTYPE html>', '<html lang="en">', '<head>',
    '<meta charset="utf-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1">',
    f'<title>{title}</title>',
    f'<meta name="description" content="{desc}">',
    '<meta name="robots" content="noindex, nofollow">',
    f'<link rel="canonical" href="{url}">']
    if not util:
        h += [
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{desc}">',
        f'<meta property="og:url" content="{url}">',
        '<meta property="og:type" content="website">',
        f'<meta property="og:site_name" content="{SITE}">',
        '<meta property="og:locale" content="en_US">',
        f'<meta property="og:image" content="{ORIGIN}/og.png">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{desc}">',
        f'<meta name="twitter:image" content="{ORIGIN}/og.png">']
    h += ['<link rel="icon" type="image/svg+xml" href="/favicon.svg">',
    '<link rel="stylesheet" href="/style.css">', '</head>', '<body>',
    '<a class="skip" href="#main">Skip to content</a>']
    return "\n".join(h)

NAV = ('<header class="top"><div class="wrap headrow"><a class="brand" href="/">M&nbsp;&amp;&nbsp;L <span>Painting</span></a>'
       '<nav class="links"><a href="/services">Services</a><a href="/interior-painting">Interior</a>'
       '<a href="/exterior-painting">Exterior</a><a href="/contact">Contact</a></nav></div></header>')
TAPE = '<div class="tape" aria-hidden="true"></div>'

FOOTER = f'''<footer>
  <div class="wrap footgrid">
    <div class="footid">
      <span class="brand">M&nbsp;&amp;&nbsp;L <span>Painting</span></span>
      <p class="footline">Interior &amp; exterior house painting — Vancouver, Washington.</p>
      <p class="footline muted">{STREET}, {CITY}, {ST} {ZIP} &middot; <a href="{TEL}">{PHONE}</a> &middot; <a href="mailto:{EMAIL}">{EMAIL}</a> &middot; <a href="{FB}">Facebook</a></p>
    </div>
    <nav class="footlinks" aria-label="Footer">
      <a href="/services">Services</a><a href="/interior-painting">Interior</a><a href="/exterior-painting">Exterior</a><a href="/contact">Contact</a>
    </nav>
    <p class="copy">© 2026 {SITE} &middot; {CITY}, {ST}</p>
  </div>
</footer>'''

def crumbs(trail):
    parts = ['<a href="/">Home</a>']
    for label, href in trail[:-1]:
        parts.append(f'<a href="{href}">{label}</a>')
    parts.append(trail[-1][0])
    return '<p class="crumbs">' + ' › '.join(parts) + '</p>'

def ld_block(data):
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=1) + '\n</script>'

def breadcrumb_ld(trail):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"}]
    for i, (label, href) in enumerate(trail, start=2):
        items.append({"@type": "ListItem", "position": i, "name": label,
                      "item": ORIGIN + ("/" if href == "/" else href)})
    return ld_block({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})

CTA = f'''<section class="quote">
  <div class="wrap quotain">
    <h2>Rated 5.0 on Google. Pick up the phone.</h2>
    <p class="deck">16012 NE 26th St, {CITY}, {ST} {ZIP} &middot; office Mon–Fri 9–5.</p>
    <div class="cta-row">
      <a class="btn fill" href="/contact">Get a quote</a>
      <a class="btn line" href="{TEL}">Call {PHONE}</a>
    </div>
  </div>
</section>'''

MAP = (f'<iframe title="Map — {SITE}, {STREET}, {CITY}, {ST} {ZIP}" src="{MAPQ}" loading="lazy"></iframe>')

STATS = '''<section class="stats">
  <div class="wrap statgrid">
    <div class="stat"><p><b>5.0</b><span>rated on Google</span></p></div>
    <div class="stat"><p><b>9–5</b><span>office hours, Mon–Fri</span></p></div>
    <div class="stat"><p><b>98684</b><span>Vancouver, Washington shop</span></p></div>
  </div>
</section>'''

PROCESS = '''<section class="block">
  <div class="wrap">
    <p class="eyebrow">How a job runs</p>
    <h2>Prep is the job</h2>
    <div class="steps">
      <div class="step"><p class="num">1</p><h3>Scope</h3><p>Call or send the form — surfaces, prep and price get agreed before a drop cloth goes down.</p></div>
      <div class="step"><p class="num">2</p><h3>Prep</h3><p>Mask, patch, sand, prime. Coatings only last as long as the surface under them.</p></div>
      <div class="step"><p class="num">3</p><h3>Paint</h3><p>Cut-ins by hand, even coats, working a room at a time so the house keeps running.</p></div>
      <div class="step"><p class="num">4</p><h3>Walk</h3><p>Final walkthrough with you, touch-ups on the spot, everything back where it came from.</p></div>
    </div>
  </div>
</section>'''

def faq(items):
    body = ''.join(f'<div class="qa"><h3>{q}</h3><p>{a}</p></div>' for q, a in items)
    return f'<section class="block"><div class="wrap"><p class="eyebrow">Good questions</p><h2>Before you call</h2><div class="fa grid2">{body}</div></div></section>'

def faq_ld(items):
    return ld_block({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]})

def service_ld(name, desc):
    return ld_block([
        {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc,
         "areaServed": {"@type": "Place", "name": CITY_FULL}, "provider": {"@id": ORIGIN + "/#business"}}])

PAGES = {}

# ---------------------------------------------------------------- home
home_ld = ld_block({
 "@context": "https://schema.org", "@type": "HousePainter", "@id": ORIGIN + "/#business",
 "name": SITE,
 "telephone": "+1-360-798-2333", "email": EMAIL,
 "address": {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": CITY,
             "addressRegion": ST, "postalCode": ZIP, "addressCountry": "US"},
 "url": ORIGIN + "/", "logo": ORIGIN + "/og.png", "image": ORIGIN + "/og.png",
 "sameAs": [FB], "areaServed": CITY_FULL})

PAGES["/index.html"] = head(
 "Interior &amp; Exterior House Painting — M &amp; L Painting, Vancouver WA",
 "M & L Painting — interior and exterior house painting in Vancouver, Washington. Rated 5.0 on Google. (360) 798-2333, office Mon–Fri 9–5.", "/") + f'''
{NAV}
{TAPE}
<main id="main">

<section class="hero">
  <div class="wrap herogrid">
    <div>
      <p class="eyebrow">House painting &middot; {CITY}, {ST}</p>
      <h1>The 5.0-rated paint crew on the northeast side.</h1>
      <p class="deck">M &amp; L Painting works homes inside and out from our {STREET} shop — prep-first paint work, rated 5.0 on Google.</p>
      <div class="cta-row">
        <a class="btn fill" href="/contact">Get a quote</a>
        <a class="btn line" href="{TEL}">Call {PHONE}</a>
      </div>
      <p class="telhint">Office Mon–Fri 9–5 — or send the job details on the <a href="/contact">quote page</a> any time.</p>
    </div>
    <div class="mark" aria-hidden="true"><p class="big5">5.0</p><p class="markcap">Google rating</p></div>
  </div>
</section>

{STATS}

<section class="block">
  <div class="wrap">
    <p class="eyebrow">What we paint</p>
    <h2>Inside, outside, or both at once</h2>
    <p class="lead">A painting company for houses in {CITY_FULL} — rooms and trim on the inside, siding and trim on the outside, scoped as one job or two.</p>
    <div class="cards">
      <div class="card">
        <div class="tab" aria-hidden="true"></div>
        <h3>Interior painting</h3>
        <p>Rooms, hallways, ceilings, trim and doors — patched, primed and rolled, with cut-in lines you can stand next to.</p>
        <a class="go" href="/interior-painting">Interior details &rarr;</a>
      </div>
      <div class="card">
        <div class="tab" aria-hidden="true"></div>
        <h3>Exterior painting</h3>
        <p>Siding, trim, fascia and doors — cleaned, scraped and caulked before the finish coats, built for west-side weather.</p>
        <a class="go" href="/exterior-painting">Exterior details &rarr;</a>
      </div>
      <div class="card">
        <div class="tab" aria-hidden="true"></div>
        <h3>Not sure which you need?</h3>
        <p>Most repaints get decided on the scope walk — we look at the surfaces together and price what actually needs paint.</p>
        <a class="go" href="/contact">Set up a quote &rarr;</a>
      </div>
    </div>
  </div>
</section>

{PROCESS}
{CTA}

</main>
{TAPE}
{FOOTER}
{home_ld}
</body>
</html>
'''

# ---------------------------------------------------------------- services
svc_ld = ld_block({"@context": "https://schema.org", "@graph": [
 {"@type": "Service", "name": "Interior painting", "areaServed": {"@type": "Place", "name": CITY_FULL}, "provider": {"@id": ORIGIN + "/#business"}},
 {"@type": "Service", "name": "Exterior painting", "areaServed": {"@type": "Place", "name": CITY_FULL}, "provider": {"@id": ORIGIN + "/#business"}}]})
PAGES["/services.html"] = head(
 "Painting Services — M &amp; L Painting, Vancouver WA",
 "Interior and exterior house painting in Vancouver, Washington. See what each job covers, how prep works, and get a quote. (360) 798-2333.", "/services") + f'''
{NAV}
{TAPE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    {crumbs([("Services", "/services")])}
    <p class="eyebrow">Services</p>
    <h1>Two kinds of paint work, done the long way</h1>
    <p class="deck">Every quote starts with the surfaces — what they are, what they need, what it costs. No hourly guesses.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <div class="cards wide2">
      <div class="card">
        <div class="tab" aria-hidden="true"></div>
        <h3>Interior painting</h3>
        <p>Full rooms and partial refreshes: walls, ceilings, trim, baseboards, doors, closets and hallways. Patch, sand, prime, coat — in that order, every time.</p>
        <a class="go" href="/interior-painting">Interior details &rarr;</a>
      </div>
      <div class="card">
        <div class="tab" aria-hidden="true"></div>
        <h3>Exterior painting</h3>
        <p>Siding, trim, fascia, soffits, doors and porch surfaces. Prep starts with cleaning and ends with caulk; finish coats go on after the house is ready.</p>
        <a class="go" href="/exterior-painting">Exterior details &rarr;</a>
      </div>
    </div>
    <div class="notecard">
      <p class="eyebrow">Both at once</p>
      <p>Whole-house repaints are commonly scoped inside and outside together — one visit, one price sheet, one crew timeline.</p>
    </div>
  </div>
</section>

{PROCESS}
{CTA}

</main>
{TAPE}
{FOOTER}
{svc_ld}
{breadcrumb_ld([("Services", "/services")])}
</body>
</html>
'''

# ---------------------------------------------------------------- interior
int_faq = [
 ("What surfaces does an interior job cover?",
  "Room walls and ceilings, hallways, closets, trim, baseboards and doors — the full envelope of the rooms in scope, not just the big flat walls."),
 ("Is patching and prep included?",
  "It comes first: nail pops and patches filled, sanding smooth, dust killed, priming where bare or repaired. That is the half of the job cheap quotes skip."),
 ("Do you move furniture out of the way?",
  "Furniture gets shifted, covered and worked around as part of prep. Empty rooms go faster, but it is not required."),
 ("How does pricing work?",
  f"By scope, not by guess. Call {PHONE} during office hours or send the contact form — surfaces and prep set the price, and you see it before work starts.")]
PAGES["/interior-painting.html"] = head(
 "Interior Painting — M &amp; L Painting, Vancouver WA",
 "Interior house painting in Vancouver, Washington — rooms, ceilings, trim and doors, patched and primed before the finish coats. Rated 5.0 on Google.", "/interior-painting") + f'''
{NAV}
{TAPE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    {crumbs([("Services", "/services"), ("Interior painting", "/interior-painting")])}
    <p class="eyebrow">Service &middot; Interior</p>
    <h1>Interior paint that survives real life</h1>
    <p class="deck">Hall scuffs, kitchen grease, closet-door edges — interior paint fails at the prep, not the color. The prep gets fixed first, then the coat goes on.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <p class="eyebrow">What gets covered</p>
    <h2>The usual scope</h2>
    <div class="specs">
      <div class="spec"><h3>Walls &amp; ceilings</h3><p>Full rooms or accent walls — roller coverage on walls, brush work where the roller can&#39;t reach.</p></div>
      <div class="spec"><h3>Trim, base &amp; doors</h3><p>Cut lines at ceiling and base, gloss on trim and doors so every edge reads sharp.</p></div>
      <div class="spec"><h3>Hallways &amp; stairs</h3><p>Worn high-touch walls and banisters, worked section by section so the house keeps functioning.</p></div>
      <div class="spec"><h3>Closets &amp; bonus rooms</h3><p>The cheap fast rooms too — primed and coated, not left as an afterthought.</p></div>
    </div>
  </div>
</section>

{PROCESS}
{faq(int_faq)}
{CTA}

</main>
{TAPE}
{FOOTER}
{service_ld("Interior painting", "Interior house painting in Vancouver, Washington — walls, ceilings, trim and doors, fully prepped before finish coats.")}
{faq_ld(int_faq)}
{breadcrumb_ld([("Services", "/services"), ("Interior painting", "/interior-painting")])}
</body>
</html>
'''

# ---------------------------------------------------------------- exterior
ext_faq = [
 ("What surfaces does an exterior job cover?",
  "Siding, trim, fascia, soffits, doors and porch surfaces — the shell of the house, painted as one system, not one wall at a time."),
 ("Is the outside cleaned before painting?",
  "Exterior prep starts with cleaning, then scraping and caulking, before any new coat goes on. Paint over dirt or open gaps peels right back off."),
 ("When is the best time to paint the outside?",
  f"West-side scheduling follows the dry stretches. Call {PHONE} when the project is on your calendar and we&#39;ll talk timing against the season."),
 ("Can this be combined with an interior job?",
  "Interior and exterior are commonly scoped together — one crew, one schedule, one walkthrough at the end.")]
PAGES["/exterior-painting.html"] = head(
 "Exterior Painting — M &amp; L Painting, Vancouver WA",
 "Exterior house painting in Vancouver, Washington — siding, trim, doors and porches cleaned, caulked and coated. Rated 5.0 on Google.", "/exterior-painting") + f'''
{NAV}
{TAPE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    {crumbs([("Services", "/services"), ("Exterior painting", "/exterior-painting")])}
    <p class="eyebrow">Service &middot; Exterior</p>
    <h1>A paint job built for west-side weather</h1>
    <p class="deck">Rain, sun and freeze-thaw attack the outside from every direction at once. Exterior paint earns its years in the prep — cleaning, scraping, caulking — before the finish coats.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <p class="eyebrow">What gets covered</p>
    <h2>The usual scope</h2>
    <div class="specs">
      <div class="spec"><h3>Siding</h3><p>Washed, scraped, spot-primed and coated — lap siding and flat surfaces, worked so the lap lines stay clean.</p></div>
      <div class="spec"><h3>Trim, fascia &amp; soffits</h3><p>The edges that decide how the house reads — caulked tight and painted smooth.</p></div>
      <div class="spec"><h3>Doors &amp; porch surfaces</h3><p>Entry doors, porch rails and columns get the same finish system as the rest of the shell.</p></div>
      <div class="spec"><h3>Gutter &amp; downspout color</h3><p>Coordinated or contrast — decided in the scope so the hardware matches the plan.</p></div>
    </div>
  </div>
</section>

{faq(ext_faq)}
{CTA}

</main>
{TAPE}
{FOOTER}
{service_ld("Exterior painting", "Exterior house painting in Vancouver, Washington — siding, trim, doors and porches cleaned, caulked and coated.")}
{faq_ld(ext_faq)}
{breadcrumb_ld([("Services", "/services"), ("Exterior painting", "/exterior-painting")])}
</body>
</html>
'''

# ---------------------------------------------------------------- contact
PAGES["/contact.html"] = head(
 "Contact &amp; Quotes — M &amp; L Painting, Vancouver WA",
 "Get a painting quote in Vancouver, Washington — call (360) 798-2333 Mon–Fri 9–5 or send the form anytime. 16012 NE 26th St, Vancouver WA 98684.", "/contact") + f'''
{NAV}
{TAPE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    {crumbs([("Contact", "/contact")])}
    <p class="eyebrow">Contact</p>
    <h1>Tell us about the surfaces</h1>
    <p class="deck">Rooms, siding, a whole house — describe it and we&#39;ll scope it and price it back to you.</p>
  </div>
</section>

<section class="block">
  <div class="wrap cgrid">
    <form class="form" method="post" action="/contact">
      <label for="f-name">Your name<input id="f-name" name="name" type="text" maxlength="120" required></label>
      <label for="f-phone">Phone (optional)<input id="f-phone" name="phone" type="tel" maxlength="60"></label>
      <label for="f-email">Email<input id="f-email" name="email" type="email" maxlength="120"></label>
      <label for="f-msg">What needs painting<textarea id="f-msg" name="message" rows="6" maxlength="4000" required></textarea></label>
      <button class="btn fill" type="submit">Send the details</button>
      <p class="formnote">The form goes straight to the business — no middleman, no mailing list.</p>
    </form>
    <aside class="cinfo">
      <div class="callbox">
        <p class="eyebrow">Phone &amp; hours</p>
        <p class="bignum"><a href="{TEL}">{PHONE}</a></p>
        <p class="muted">Office Mon–Fri 9–5 &middot; email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div class="addr">
        <p class="eyebrow">Where</p>
        <p>{STREET}<br>{CITY}, {ST} {ZIP}</p>
      </div>
      <div class="mapwrap">{MAP}</div>
    </aside>
  </div>
</section>

</main>
{TAPE}
{FOOTER}
{breadcrumb_ld([("Contact", "/contact")])}
</body>
</html>
'''

# ---------------------------------------------------------------- privacy
PAGES["/privacy.html"] = head(
 "Privacy — M &amp; L Painting, Vancouver WA",
 "How this site handles the contact form: no cookies, no third-party trackers, nothing served from other companies' servers.", "/privacy") + f'''
{NAV}
{TAPE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    {crumbs([("Privacy", "/privacy")])}
    <p class="eyebrow">Privacy</p>
    <h1>What this site knows about you</h1>
    <p class="deck">Very little, on purpose.</p>
  </div>
</section>

<section class="prose">
  <div class="wrap narrow">
    <h2>The contact form</h2>
    <p>When you send the contact form, {SITE} receives your name, message, and any phone number or email you add — used only to answer you and quote the job. Messages are delivered by email and kept no longer than needed to follow up.</p>
    <h2>No trackers</h2>
    <p>This site loads no third-party scripts and sets no advertising or analytics cookies. The stylesheet, fonts and images are all served from this site itself. Nothing about your visit is assembled into a profile.</p>
    <h2>Questions</h2>
    <p>Want something kept or removed from the email trail? Call {PHONE} or write {EMAIL} and say the word.</p>
  </div>
</section>

</main>
{TAPE}
{FOOTER}
{breadcrumb_ld([("Privacy", "/privacy")])}
</body>
</html>
'''

# ---------------------------------------------------------------- thanks
PAGES["/thanks.html"] = head(
 "Thanks — M &amp; L Painting",
 "Your message is on its way to M & L Painting, Vancouver Washington.", "/thanks", util=True) + f'''
{NAV}
{TAPE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    <p class="eyebrow">Sent</p>
    <h1>Your message is on its way</h1>
    <p class="deck">It landed with {SITE} — watch for the reply.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cta-row" style="justify-content:flex-start">
      <a class="btn fill" href="/">Back to home</a>
      <a class="btn line dark" href="/services">Browse services</a>
    </div>
  </div>
</section>

</main>
{TAPE}
{FOOTER}
</body>
</html>
'''

# ---------------------------------------------------------------- 404
PAGES["/404.html"] = head(
 "Page not found — M &amp; L Painting",
 "That page is not here. Start over at M & L Painting, Vancouver Washington.", "/404", util=True) + f'''
{NAV}
{TAPE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    <p class="eyebrow">404</p>
    <h1>That page took a wrong turn</h1>
    <p class="deck">The paint is down the hall. Try one of these:</p>
    <div class="cta-row" style="justify-content:flex-start">
      <a class="btn fill" href="/">Home</a>
      <a class="btn line dark" href="/services">Services</a>
      <a class="btn line dark" href="/contact">Contact</a>
    </div>
  </div>
</section>

</main>
{TAPE}
{FOOTER}
</body>
</html>
'''

# ---------------------------------------------------------------- robots + sitemap
robots = f"""User-agent: *
Allow: /

Sitemap: {ORIGIN}/sitemap.xml
"""
sitemap_pages = ["/", "/services", "/interior-painting", "/exterior-painting", "/contact", "/privacy"]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
    "".join(f"  <url><loc>{ORIGIN}{p}</loc></url>\n" for p in sitemap_pages) + "</urlset>\n"

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
for path, html in PAGES.items():
    p = os.path.join(out, path.lstrip("/"))
    os.makedirs(os.path.dirname(p) or out, exist_ok=True)
    body = BUILT + html
    open(p, "w", encoding="utf8").write(body)
    print(f"{len(body):>7}  {path}")
open(os.path.join(out, "robots.txt"), "w").write(robots); print(f"{len(robots):>7}  /robots.txt")
open(os.path.join(out, "sitemap.xml"), "w").write(sitemap); print(f"{len(sitemap):>7}  /sitemap.xml")
print("pages:", len(PAGES))
