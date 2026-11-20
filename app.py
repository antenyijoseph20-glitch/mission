from __future__ import annotations
import streamlit as st
from milestones import LAYERS, MILESTONES, validate_data

st.set_page_config(page_title="Interactive AI Timeline Pyramid", page_icon="🧠", layout="wide", initial_sidebar_state="expanded")
validate_data()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

:root {
    --bg: #0B1220;
    --panel: #162235;
    --panel-soft: #1E293B;
    --accent: #2DD4BF;
    --accent-hover: #5EEAD4;
    --text: #F1F5F9;
    --muted: #B0BECF;
    --border: rgba(148, 163, 184, 0.22);
    --focus: #FACC15;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 50% -15%,
        #203B55 0%, #101B2C 42%, var(--bg) 100%);
    color: var(--text);
}

.block-container {
    max-width: 1440px;
    padding: 2rem 2rem 3rem;
}

h1, h2, h3, h4 {
    font-family: 'Manrope', sans-serif;
    color: var(--text);
    letter-spacing: -0.025em;
}

p, li {
    color: var(--muted);
    line-height: 1.7;
}

.hero-kicker {
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 0.17em;
    font-size: 0.75rem;
    font-weight: 700;
}

.hero-title {
    font-family: 'Manrope', sans-serif;
    font-size: clamp(2rem, 5vw, 3.7rem);
    line-height: 1.08;
    font-weight: 800;
    margin: 0.5rem 0 0.8rem;
    color: #F8FAFC;
    overflow-wrap: anywhere;
}

.hero-copy {
    color: #C1CDDB;
    font-size: 1.04rem;
    max-width: 800px;
    line-height: 1.75;
}

.metric-card {
    background: linear-gradient(145deg, #1C2B40, #142136);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 16px 18px;
    min-height: 84px;
    box-shadow: 0 8px 24px rgba(0,0,0,.12);
}

.metric-number {
    font-family: 'Manrope', sans-serif;
    font-size: 1.65rem;
    font-weight: 800;
    color: var(--accent);
}

.metric-label {
    color: var(--muted);
    font-size: 0.8rem;
    margin-top: 3px;
}

.layer-shell {
    border: 1px solid var(--border);
    border-radius: 15px;
    background: linear-gradient(110deg, #20334A, #16263B);
    padding: 13px 15px 15px;
    margin: 0 auto 9px;
    box-shadow: 0 7px 20px rgba(0,0,0,.15);
    transition: border-color .2s ease, box-shadow .2s ease;
}

.layer-shell.active-layer {
    border-color: var(--accent);
    box-shadow: 0 0 0 1px rgba(45,212,191,.2),
                0 8px 25px rgba(0,0,0,.2);
}

.layer-heading {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 8px;
}

.layer-name {
    color: #F1F5F9;
    font-weight: 700;
    font-size: .9rem;
}

.layer-period {
    color: #B0BECF;
    font-size: .76rem;
}

.stButton > button {
    width: 100%;
    min-height: 44px;
    border-radius: 10px;
    border: 1px solid rgba(148,163,184,.3);
    background: #132238;
    color: #EAF2F8;
    font-weight: 600;
    transition: all .18s ease;
    overflow-wrap: anywhere;
}

.stButton > button:hover {
    border-color: var(--accent);
    background: rgba(45,212,191,.12);
    color: var(--accent-hover);
}

.stButton > button:focus-visible,
.stTextInput input:focus-visible,
.stSelectbox div[role="combobox"]:focus-visible {
    outline: 3px solid var(--focus) !important;
    outline-offset: 3px;
}

.stTextInput input,
.stSelectbox div[data-baseweb="select"] > div {
    background: #17263A;
    color: var(--text);
    border-color: var(--border);
    border-radius: 10px;
}

.stTextInput label,
.stSelectbox label {
    color: #DCE6F1 !important;
    font-weight: 600;
}

.detail-card {
    background: linear-gradient(145deg, #1B2B41, #132136);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 23px;
    box-shadow: 0 10px 28px rgba(0,0,0,.16);
}

.detail-id {
    color: var(--accent);
    font-size: .76rem;
    font-weight: 700;
    letter-spacing: .12em;
}

.detail-title {
    color: #F8FAFC;
    font-family: 'Manrope', sans-serif;
    font-weight: 800;
    font-size: clamp(1.3rem, 2.5vw, 1.7rem);
    line-height: 1.25;
    margin: .5rem 0 .7rem;
    overflow-wrap: anywhere;
}

.detail-meta {
    color: #B0BECF;
    font-size: .88rem;
    line-height: 1.6;
    margin-bottom: 1rem;
}

.detail-section {
    color: #F1F5F9;
    font-weight: 700;
    font-size: 1rem;
    margin-top: 1.3rem;
    margin-bottom: .4rem;
}

.detail-body {
    color: #C1CDDB;
    line-height: 1.75;
    overflow-wrap: anywhere;
}

.source-note {
    color: #F5D99C;
    font-size: .87rem;
    border-left: 3px solid #D6AC59;
    padding: .7rem .9rem;
    background: rgba(214,172,89,.09);
    margin-top: 1rem;
    border-radius: 0 8px 8px 0;
}

.pill {
    display: inline-block;
    border: 1px solid rgba(45,212,191,.35);
    background: rgba(45,212,191,.09);
    color: #7DE8D7;
    padding: 5px 10px;
    border-radius: 30px;
    font-size: .73rem;
    margin: 3px 5px 3px 0;
    overflow-wrap: anywhere;
}

hr {
    border-color: var(--border);
}

[data-testid="stSidebar"] {
    background: #0D1727;
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #C1CDDB;
}

[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] label {
    color: var(--text) !important;
}

.stCaption {
    color: var(--muted) !important;
}

a {
    color: #5EEAD4 !important;
    text-decoration-thickness: 1px;
    text-underline-offset: 3px;
}

a:hover {
    color: #99F6E4 !important;
}

@media (max-width: 900px) {
    .block-container {
        padding: 1.5rem 1.25rem 2.5rem;
    }

    .detail-card {
        padding: 19px;
    }
}

@media (max-width: 600px) {
    .block-container {
        padding: 1.1rem .85rem 2rem;
    }

    .hero-title {
        font-size: 2rem;
    }

    .hero-copy {
        font-size: .94rem;
    }

    .metric-card {
        padding: 12px;
        min-height: 75px;
    }

    .metric-number {
        font-size: 1.35rem;
    }

    .metric-label {
        font-size: .7rem;
    }

    .layer-shell {
        padding: 10px;
    }

    .layer-heading {
        align-items: flex-start;
    }

    .layer-name {
        font-size: .82rem;
    }

    .layer-period {
        font-size: .72rem;
    }

    .detail-card {
        padding: 16px;
        border-radius: 14px;
    }

    .detail-title {
        font-size: 1.3rem;
    }

    .detail-meta {
        font-size: .82rem;
    }

    .detail-body {
        font-size: .93rem;
    }

    .pill {
        line-height: 1.5;
    }

    .stButton > button {
        min-height: 46px;
        font-size: .85rem;
    }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        transition-duration: .01ms !important;
        animation-duration: .01ms !important;
        scroll-behavior: auto !important;
    }
}

/* Darker timeline layers and milestone markers */
.layer-shell {
    background: linear-gradient(
        120deg,
        #17263B,
        #101D30
    ) !important;
    border-color: #40536B !important;
}

.layer-shell.active-layer {
    background: linear-gradient(
        120deg,
        #193448,
        #12283A
    ) !important;
    border-color: #2DD4BF !important;
}

/* Force milestone buttons to use dark backgrounds */
.stButton > button {
    background-color: #0B1729 !important;
    color: #F1F5F9 !important;
    border: 1px solid #40536B !important;
}

/* Hover and keyboard focus */
.stButton > button:hover {
    background-color: #193448 !important;
    color: #5EEAD4 !important;
    border-color: #2DD4BF !important;
}

.stButton > button:focus-visible {
    outline: 3px solid #FACC15 !important;
    outline-offset: 3px;
}

/* Disabled navigation buttons */
.stButton > button:disabled {
    background-color: #111C2D !important;
    color: #8493A7 !important;
    border-color: #344256 !important;
    opacity: 1 !important;
}


/* Pyramid guide and visual legend */
.pyramid-legend {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 12px 22px;
    background: #142238;
    border: 1px solid #40536B;
    border-radius: 13px;
    padding: 13px 16px;
    margin: 12px 0 20px;
}

.legend-item {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #DCE6F1;
    font-size: .83rem;
}

.legend-swatch {
    width: 17px;
    height: 17px;
    flex: 0 0 17px;
    border-radius: 5px;
    background: #0B1729;
    border: 1px solid #60748D;
}

.legend-swatch.selected {
    background: #16483F;
    border: 2px solid #2DD4BF;
}

.legend-direction {
    color: #B0BECF;
    font-size: .82rem;
    line-height: 1.6;
    width: 100%;
}

.stButton > button[kind="primary"] {
    background: #16483F !important;
    color: #99F6E4 !important;
    border: 2px solid #2DD4BF !important;
    font-weight: 700 !important;
    box-shadow: 0 0 0 1px rgba(45,212,191,.12);
}

.stButton > button[kind="primary"]:hover {
    background: #1B5B50 !important;
    color: #CCFBF1 !important;
}


/* Consistent spacing between milestone profile labels */
.profile-tags {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    margin-top: 12px;
}

.profile-tags .pill {
    margin: 0;
    line-height: 1.5;
}
\n
/* Consistent spacing between milestone profile labels */
.profile-tags {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    margin-top: 12px;
}

.profile-tags .pill {
    margin: 0;
    line-height: 1.5;
}
\n</style>
""", unsafe_allow_html=True)

if "selected_id" not in st.session_state:
    st.session_state.selected_id = "AI-029"
def reset_timeline_filter():
    st.session_state.layer_filter_widget = "All layers"

by_id = {m["id"]: m for m in MILESTONES}
selected = by_id.get(st.session_state.selected_id, MILESTONES[-1])

st.markdown('<div class="hero-kicker">A visual history of artificial intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">The AI Timeline Pyramid</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-copy">Explore 29 landmark developments across six chronological layers — from the mathematical foundations of machine intelligence to today’s generative models and AI agents. Select any milestone to explore its people, ideas, significance and references.</div>', unsafe_allow_html=True)

m1,m2,m3 = st.columns(3)
for col, number, label in [(m1,"29","Historical milestones"),(m2,"6","Chronological layers"),(m3,"1943 → now","Timeline coverage")]:
    with col: st.markdown(f'<div class="metric-card"><div class="metric-number">{number}</div><div class="metric-label">{label}</div></div>',unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## Explore the timeline")
    search = st.text_input("Search milestones", placeholder="Try ‘Transformer’ or ‘Turing’", help="Search milestone IDs, dates, contributors, AI subfields and historical descriptions.")
    layer_options = ["All layers"] + [f"Layer {l['id']}: {l['name']}" for l in LAYERS]
    chosen_layer = st.selectbox(
        "Filter by layer",
        layer_options,
        index=0,
        key="layer_filter_widget"
    )
    jump = st.selectbox("Quick jump to milestone", [f"{m['id']} — {m['title']}" for m in MILESTONES], index=next((i for i,m in enumerate(MILESTONES) if m['id']==st.session_state.selected_id),len(MILESTONES)-1))
    if st.button("Open selected milestone", use_container_width=True):
        st.session_state.selected_id = jump.split(" — ")[0]
        st.rerun()
    st.divider()
    st.caption("The six layers are chronological. The broad base represents the earliest foundations; the narrow apex represents the most recent developments.")
    st.caption("Source access note: AI-002 includes a bibliographic primary-source record; a stable, freely accessible full-text copy remains outstanding.")

query = search.strip().lower()
filtered = []
for m in MILESTONES:
    layer_label = f"Layer {m['layer']}: {LAYERS[m['layer']-1]['name']}"
    if chosen_layer != "All layers" and chosen_layer != layer_label:
        continue
    searchable = " ".join([m['id'],m['date'],m['title'],m['contributors'],m['subfield'],m['what'],m['approach'],m['significance'],m['impact'],m['limitations']]).lower()
    if query and query not in searchable:
        continue
    filtered.append(m)

if st.session_state.selected_id not in [m['id'] for m in MILESTONES]:
    st.session_state.selected_id = MILESTONES[-1]['id']
selected = by_id[st.session_state.selected_id]

st.markdown("### Explore the six layers")
st.caption(f"Showing {len(filtered)} of 29 milestones. Choose a milestone marker to open its historical profile.")


st.markdown("""
<div class="pyramid-legend">
    <div class="legend-item">
        <span class="legend-swatch selected"></span>
        <span>Selected milestone</span>
    </div>
    <div class="legend-item">
        <span class="legend-swatch"></span>
        <span>Other milestones</span>
    </div>
    <div class="legend-direction">
        <strong>How to read the pyramid:</strong>
        The apex at the top represents the most recent developments.
        The broad base represents the earliest foundations.
        Select any milestone button to view its historical profile.
    </div>
</div>
""", unsafe_allow_html=True)


# The pyramid narrows toward the top; layer 6 is the apex and layer 1 is the broad base.
widths = {6:2,5:3,4:4,3:5,2:6,1:7}
for layer in reversed(LAYERS):
    lid = layer["id"]
    layer_items = [m for m in filtered if m["layer"] == lid]
    if not layer_items:
        continue
    side_weight = max(1, 7 - widths[lid])
    left, center, right = st.columns([side_weight, widths[lid], side_weight], gap="small")
    target = center
    with target:
        is_active = selected["layer"] == lid
        st.markdown(f'<div class="layer-shell {"active-layer" if is_active else ""}"><div class="layer-heading"><span class="layer-name">LAYER {lid} · {layer["name"]}</span><span class="layer-period">{layer["period"]}</span></div></div>',unsafe_allow_html=True)
        # Each marker is a real Streamlit button with a descriptive accessible label.
        cols = st.columns(min(4,len(layer_items)),gap="small")
        for idx,m in enumerate(layer_items):
            with cols[idx % len(cols)]:
                label = f"{m['id']}\n{m['date']}"
                if st.button(label,key=f"milestone_{m['id']}",use_container_width=True,help=f"Open {m['title']} ({m['date']})",type="primary" if m["id"] == selected["id"] else "secondary"):
                    st.session_state.selected_id = m["id"]
                    st.rerun()

st.divider()
left_col, right_col = st.columns([1.55,1],gap="large")
with left_col:
    st.markdown("### Milestone profile")
    st.markdown(f'''<div class="detail-card"><div class="detail-id">{selected['id']} · LAYER {selected['layer']}</div><div class="detail-title">{selected['title']}</div><div class="detail-meta">{selected['date']} &nbsp;·&nbsp; {selected['contributors']}</div><div class="profile-tags"><div class="profile-tags"><span class="pill">{LAYERS[selected['layer']-1]['name']}</span><span class="pill">{selected['subfield']}</span></div></div></div>''',unsafe_allow_html=True)
    for heading,key in [("What happened","what"),("How it worked","approach"),("Why it mattered","significance"),("Real-world impact","impact"),("Limitations and historical context","limitations")]:
        st.markdown(f'<div class="detail-section">{heading}</div><div class="detail-body">{selected[key]}</div>',unsafe_allow_html=True)
    if selected.get("source_note"):
        st.markdown(f'<div class="source-note">{selected["source_note"]}</div>',unsafe_allow_html=True)
with right_col:
    st.markdown("### References and navigation")
    st.caption("Reference titles open their cited destination in a new browser tab. Final destination-by-destination testing is part of release validation.")
    for i,(title,url) in enumerate(selected["sources"],1):
        st.markdown(f"**{i}. [{title}]({url})**")
    st.divider()
    current_index = next(i for i,m in enumerate(MILESTONES) if m["id"] == selected["id"])
    prev_col,next_col = st.columns(2)
    with prev_col:
        if current_index > 0:
            if st.button("← Previous",use_container_width=True):
                st.session_state.selected_id = MILESTONES[current_index-1]["id"]
                st.rerun()
        else:
            st.button("← Previous",disabled=True,use_container_width=True)
    with next_col:
        if current_index < len(MILESTONES)-1:
            if st.button("Next →",use_container_width=True):
                st.session_state.selected_id = MILESTONES[current_index+1]["id"]
                st.rerun()
        else:
            st.button("Next →",disabled=True,use_container_width=True)
    st.button(
        "Back to full timeline",
        use_container_width=True,
        on_click=reset_timeline_filter
    )

st.divider()
st.markdown("<div style='text-align:center;color:#8fa4ba;font-size:.8rem'>Interactive AI Timeline Pyramid · Historical scope: 1943–present · 29 approved milestones</div>",unsafe_allow_html=True)
