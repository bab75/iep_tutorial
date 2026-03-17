"""Step 11 — Certificate of Completion"""
import streamlit as st, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
st.set_page_config(page_title="Certificate · IEP Tutorial", page_icon="🎓", layout="wide")
from utils.engine import *
apply_theme(); init_session(); sidebar_nav()

rc      = get_role_config()
done    = steps_completed()
total   = TOTAL_STEPS
avg     = st.session_state.get("total_score", 0)
role    = get_role() or "Learner"

if done < total:
    st.warning(f"You have completed {done} of {total} steps. Finish all steps to earn your certificate.")
    st.info("👈 Use the sidebar to navigate to remaining steps.")
    st.stop()

# ── Certificate ───────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="background:white;border:3px solid #1E3A8A;border-radius:20px;
            padding:40px;max-width:700px;margin:0 auto 24px;text-align:center;
            box-shadow:0 4px 24px rgba(30,58,138,0.12);">
    <div style="font-size:3rem;margin-bottom:8px;">🎓</div>
    <div style="color:#94A3B8;font-size:0.8rem;letter-spacing:.15em;
                text-transform:uppercase;margin-bottom:6px;">Certificate of Completion</div>
    <div style="font-family:'Nunito',sans-serif;font-weight:900;
                color:#1E3A8A;font-size:1.8rem;margin-bottom:6px;">
        IEP Process Tutorial</div>
    <div style="color:#64748B;font-size:0.88rem;margin-bottom:18px;">
        This certifies that</div>
    <div style="font-family:'Nunito',sans-serif;font-weight:900;
                color:#1E293B;font-size:1.5rem;border-bottom:2px solid #E2E8F0;
                padding-bottom:14px;margin-bottom:14px;">
        {rc['icon']} {role}</div>
    <div style="color:#475569;font-size:0.88rem;line-height:1.8;margin-bottom:20px;">
        has successfully completed all <b>10 steps</b> of the IEP Process Tutorial,
        demonstrating knowledge of the Individuals with Disabilities Education Act (IDEA),
        the complete IEP process from Child Find through dispute resolution,
        and the rights and responsibilities of every IEP team member.
    </div>
    <div style="display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-bottom:20px;">
        <div style="text-align:center;">
            <div style="font-family:'Nunito',sans-serif;font-weight:900;
                        color:#2563EB;font-size:2rem;">{done}/{total}</div>
            <div style="color:#64748B;font-size:0.75rem;">Steps Complete</div>
        </div>
        <div style="text-align:center;">
            <div style="font-family:'Nunito',sans-serif;font-weight:900;
                        color:#16A34A;font-size:2rem;">{avg}%</div>
            <div style="color:#64748B;font-size:0.75rem;">Average Score</div>
        </div>
        <div style="text-align:center;">
            <div style="font-family:'Nunito',sans-serif;font-weight:900;
                        color:#D97706;font-size:2rem;">IDEA</div>
            <div style="color:#64748B;font-size:0.75rem;">Law Basis</div>
        </div>
    </div>
    <div style="color:#94A3B8;font-size:0.75rem;">
        IEP Process Tutorial · Based on Federal IDEA Law · Applies in all 50 US States
    </div>
</div>
""", unsafe_allow_html=True)

# ── Score breakdown ───────────────────────────────────────────────────────────
st.markdown("### Your Step-by-Step Results")
cols = st.columns(5)
for i, step in enumerate(STEPS[:10]):
    with cols[i % 5]:
        score = get_step_score(step["id"])
        color = "#16A34A" if score >= 80 else "#D97706" if score >= 60 else "#DC2626"
        st.markdown(f"""
        <div style="background:white;border-radius:10px;border:1px solid #E2E8F0;
                    padding:10px;text-align:center;margin-bottom:8px;">
            <div style="font-size:1.1rem;">{step['icon']}</div>
            <div style="font-size:0.72rem;color:#64748B;margin:3px 0;">{step['title']}</div>
            <div style="font-weight:800;color:{color};font-size:1rem;">{score}%</div>
        </div>""", unsafe_allow_html=True)

# ── Key takeaways ─────────────────────────────────────────────────────────────
st.markdown("### Key Takeaways from This Tutorial")
takeaways = [
    ("Child Find is proactive", "Schools must identify suspected disabilities — parents don't have to wait to be invited into the process."),
    ("Written records matter", "Every request, every consent, every notice — in writing, dated, with a copy kept by the parent."),
    ("60 school days is the law", "From consent to evaluate → IEP meeting: 60 school days. No exceptions."),
    ("Parent = equal team member", "At every step — eligibility, IEP writing, placement — the parent is a required, equal decision maker."),
    ("Mandates are binding", "Services in the IEP are legal obligations. Missed sessions must be made up."),
    ("Stay Put protects students", "During any dispute, current placement and services cannot change without parent consent."),
    ("Four free dispute options", "State complaint, mediation, due process, court — none require accepting a bad decision."),
    ("Annual review is a deadline", "On or before the anniversary date, every year, without exception."),
]
c1, c2 = st.columns(2)
for i, (title, desc) in enumerate(takeaways):
    with (c1 if i % 2 == 0 else c2):
        st.markdown(f"""
        <div style="display:flex;gap:8px;padding:7px 0;border-bottom:1px solid #F1F5F9;">
            <span style="color:#16A34A;font-weight:700;flex-shrink:0;">✓</span>
            <div><b style="color:#1E293B;font-size:0.85rem;">{title}:</b>
            <span style="color:#64748B;font-size:0.83rem;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

# ── Reset ─────────────────────────────────────────────────────────────────────
st.markdown("<div style='margin-top:24px'></div>", unsafe_allow_html=True)
st.markdown("---")
cl, cr = st.columns([3,1])
with cl:
    st.caption("Want to retake the tutorial with a different role? Reset your progress below.")
with cr:
    if st.button("🔄 Reset & Restart", use_container_width=True):
        for key in ["role","step_scores","step_completed","quiz_answers",
                    "current_step","tutorial_started","total_score"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()
