from __future__ import annotations
import streamlit as st
from milestones import LAYERS, MILESTONES, validate_data

st.set_page_config(page_title="Interactive AI Timeline Pyramid", page_icon="🧠", layout="wide", initial_sidebar_state="expanded")
validate_data()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
:root { --ink:#eaf0f7; --muted:#a8b6c8; --line:rgba(170,190,215,.18); --panel:rgba(17,28,45,.78); --accent:#75d5c3; }
html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
.stApp { background: radial-gradient(ellipse at 50% -15%, #203d58 0%, #101c2e 45%, #0a1220 100%); color:var(--ink); }
.block-container { max-width:1400px; padding-top:2rem; padding-bottom:3rem; }
h1,h2,h3 { font-family:'Manrope',sans-serif; letter-spacing:-.035em; }
.hero-kicker { color:#8be1d1; text-transform:uppercase; letter-spacing:.18em; font-size:.73rem; font-weight:700; }
.hero-title { font-family:'Manrope',sans-serif; font-size:clamp(2rem,4vw,3.7rem); line-height:1.04; font-weight:800; margin:.45rem 0 .8rem; color:#f4f8fc; }
.hero-copy { color:#b7c6d7; font-size:1.05rem; max-width:780px; line-height:1.65; }
.metric-card { background:rgba(255,255,255,.045); border:1px solid var(--line); border-radius:16px; padding:14px 17px; min-height:78px; }
.metric-number { font-family:'Manrope'; font-size:1.55rem; font-weight:800; color:#f6fbff; }
.metric-label { color:#9fb0c4; font-size:.78rem; }
.layer-shell { border:1px solid rgba(190,210,230,.22); border-radius:16px; background:linear-gradient(110deg,rgba(42,68,91,.85),rgba(20,37,57,.9)); padding:12px 14px 14px; margin:0 auto 9px; box-shadow:0 8px 22px rgba(0,0,0,.13); }
.layer-shell.active-layer { border-color:rgba(117,213,195,.8); box-shadow:0 0 0 1px rgba(117,213,195,.18),0 8px 22px rgba(0,0,0,.2); }
.layer-heading { display:flex; justify-content:space-between; align-items:baseline; gap:12px; margin-bottom:8px; }
.layer-name { color:#edf6ff; font-weight:700; font-size:.91rem; }
.layer-period { color:#9db2c7; font-size:.76rem; white-space:nowrap; }
.stButton > button { border-radius:10px; border:1px solid rgba(196,216,235,.23); background:rgba(7,18,31,.45); color:#eaf4fb; font-weight:600; min-height:42px; transition:all .15s ease; }
.stButton > button:hover { border-color:#75d5c3; color:#9cebdc; background:rgba(117,213,195,.1); }
.stButton > button:focus-visible { outline:3px solid #f6d77a !important; outline-offset:3px; }
.detail-card { background:linear-gradient(145deg,rgba(24,42,63,.95),rgba(13,25,41,.97)); border:1px solid var(--line); border-radius:18px; padding:22px; }
.detail-id { color:#8be1d1; font-size:.76rem; font-weight:700; letter-spacing:.13em; }
.detail-title { color:#f4f8fc; font-family:'Manrope'; font-weight:800; font-size:1.55rem; line-height:1.2; margin:.4rem 0 .6rem; }
.detail-meta { color:#a8bbce; font-size:.87rem; margin-bottom:1rem; }
.detail-section { color:#dbe6f0; font-weight:700; margin-top:1.05rem; margin-bottom:.25rem; }
.detail-body { color:#b7c7d8; line-height:1.62; }
.source-note { color:#e8c98b; font-size:.85rem; border-left:3px solid #d7ad62; padding:.5rem .75rem; background:rgba(215,173,98,.08); margin-top:1rem; }
.pill { display:inline-block; border:1px solid rgba(117,213,195,.35); background:rgba(117,213,195,.09); color:#9cebdc; padding:4px 9px; border-radius:30px; font-size:.72rem; margin-right:5px; }
hr { border-color:var(--line); }
[data-testid="stSidebar"] { background:rgba(8,17,29,.92); border-right:1px solid var(--line); }
[data-testid="stSidebar"] * { color:#dce8f3; }
.stCaption { color:#9eb0c4 !important; }
a { color:#8be1d1 !important; }
@media(max-width:760px) { .block-container{padding-left:1rem;padding-right:1rem;} .layer-shell{padding:10px;} .detail-title{font-size:1.3rem;} }
</style>
""", unsafe_allow_html=True)

if "selected_id" not in st.session_state:
    st.session_state.selected_id = "AI-029"
if "layer_filter" not in st.session_state:
    st.session_state.layer_filter = "All layers"

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
    search = st.text_input("Search milestones", placeholder="Try ‘Transformer’ or ‘Turing’", help="Search titles, dates, contributors and descriptions.")
    layer_options = ["All layers"] + [f"Layer {l['id']}: {l['name']}" for l in LAYERS]
    chosen_layer = st.selectbox("Filter by layer", layer_options, index=layer_options.index(st.session_state.layer_filter) if st.session_state.layer_filter in layer_options else 0)
    st.session_state.layer_filter = chosen_layer
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
    searchable = " ".join([m['id'],m['date'],m['title'],m['contributors'],m['what'],m['significance']]).lower()
    if query and query not in searchable:
        continue
    filtered.append(m)

if st.session_state.selected_id not in [m['id'] for m in MILESTONES]:
    st.session_state.selected_id = MILESTONES[-1]['id']
selected = by_id[st.session_state.selected_id]

st.markdown("### Explore the six layers")
st.caption(f"Showing {len(filtered)} of 29 milestones. Choose a milestone marker to open its historical profile.")

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
                if st.button(label,key=f"milestone_{m['id']}",use_container_width=True,help=f"Open {m['title']} ({m['date']})"):
                    st.session_state.selected_id = m["id"]
                    st.rerun()

st.divider()
left_col, right_col = st.columns([1.55,1],gap="large")
with left_col:
    st.markdown("### Milestone profile")
    st.markdown(f'''<div class="detail-card"><div class="detail-id">{selected['id']} · LAYER {selected['layer']}</div><div class="detail-title">{selected['title']}</div><div class="detail-meta">{selected['date']} &nbsp;·&nbsp; {selected['contributors']}</div><span class="pill">{LAYERS[selected['layer']-1]['name']}</span></div>''',unsafe_allow_html=True)
    for heading,key in [("What happened","what"),("How it worked","approach"),("Why it mattered","significance"),("Influence on later technology","impact"),("Limitations and historical context","limitations")]:
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
    if st.button("Back to full timeline",use_container_width=True):
        st.session_state.layer_filter = "All layers"
        st.rerun()

st.divider()
st.markdown("<div style='text-align:center;color:#8fa4ba;font-size:.8rem'>Interactive AI Timeline Pyramid · Historical scope: 1943–present · 29 approved milestones</div>",unsafe_allow_html=True)
