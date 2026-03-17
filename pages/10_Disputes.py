"""Step 10 — Disputes & Resolution"""
import streamlit as st, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
st.set_page_config(page_title="Step 10 · IEP Tutorial", page_icon="⚖️", layout="wide")
from utils.engine import *
apply_theme(); init_session(); sidebar_nav()
page_header("⚖️", "Step 10 — Disputes & Resolution", "When things go wrong — four options every family and professional should know")
step_badge(10)

scenario_box("Two years into Alex's IEP, his parents believe the school is not providing all of his mandated speech therapy sessions. The school says the SLP has been out sick. Alex has missed 12 sessions. His parents also believe the placement is no longer appropriate — Alex has made significant progress and they want him moved to a less restrictive setting. The school disagrees. What can they do?")

info_card("You Do Not Have to Accept a Decision You Disagree With",
    "IDEA provides four formal dispute resolution options — all free of charge. "
    "Using one option does not prevent you from using others. "
    "None of these require a lawyer (though you may choose to have one).",
    "#DC2626")
law_badge("IDEA § 300.151–300.152 / § 300.506 / § 300.507", "Federal law guarantees these dispute resolution rights to every parent of a child with an IEP.")

st.markdown("## The Four Dispute Options — Side by Side")
options = [
    {
        "name": "State Complaint",
        "icon": "📬",
        "color": "#2563EB",
        "cost": "Free",
        "time": "60 days for state investigation",
        "best": "Clear IDEA violations — missed timelines, services not provided, procedural errors",
        "how": "Write to your state education department describing the specific violation. No hearing required.",
        "result": "State investigates and orders corrective action. May include compensatory services.",
        "example": "Alex missed 12 speech sessions — perfect for a state complaint.",
    },
    {
        "name": "Mediation",
        "icon": "🤝",
        "color": "#0D9488",
        "cost": "Free",
        "time": "30–60 days",
        "best": "Placement disagreements, service level disputes — when both sides want to resolve it",
        "how": "Neutral mediator helps both sides reach a voluntary agreement.",
        "result": "Binding written agreement if both parties agree. Preserves working relationship.",
        "example": "Parents want less restrictive placement — good for mediation.",
    },
    {
        "name": "Due Process Hearing",
        "icon": "🏛️",
        "color": "#D97706",
        "cost": "Free to file — legal fees possible",
        "time": "45 days after resolution period",
        "best": "Serious disagreements about eligibility, IEP content, or significant service failures",
        "how": "Formal hearing before an impartial officer. Both sides present evidence.",
        "result": "Binding legal decision. Can award compensatory education and reimbursement.",
        "example": "If mediation fails on placement — escalate to due process.",
    },
    {
        "name": "State/Federal Court",
        "icon": "⚖️",
        "color": "#7C3AED",
        "cost": "Attorney fees",
        "time": "Months to years",
        "best": "Appeals of due process decisions. Civil rights violations.",
        "how": "File in state or federal court to appeal the hearing officer's decision.",
        "result": "Court order. Full legal remedies available.",
        "example": "Last resort when all other options are exhausted.",
    },
]

cols = st.columns(4)
for col, opt in zip(cols, options):
    with col:
        st.markdown(f"""
        <div style="background:{opt['color']}0D;border:1px solid {opt['color']}40;
                    border-top:4px solid {opt['color']};border-radius:12px;
                    padding:14px;min-height:340px;">
            <div style="font-size:1.5rem;margin-bottom:6px;">{opt['icon']}</div>
            <div style="font-family:'Nunito',sans-serif;font-weight:800;
                        color:{opt['color']};font-size:0.9rem;margin-bottom:8px;">{opt['name']}</div>
            <div style="font-size:0.75rem;margin-bottom:8px;">
                <span style="background:white;border-radius:4px;padding:1px 7px;
                             color:{opt['color']};font-weight:600;">💰 {opt['cost']}</span><br>
                <span style="color:#64748B;margin-top:4px;display:block;">⏱️ {opt['time']}</span>
            </div>
            <div style="font-size:0.78rem;color:#374151;margin-bottom:6px;line-height:1.5;">
                <b>Best for:</b> {opt['best']}</div>
            <div style="font-size:0.76rem;color:#64748B;line-height:1.5;">
                <b>Result:</b> {opt['result']}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("## ⚠️ The Stay Put Rule")
st.markdown("""
<div style="background:#FEF2F2;border:2px solid #DC2626;border-radius:10px;padding:14px 18px;margin:12px 0;">
    <div style="font-weight:700;color:#DC2626;font-size:0.9rem;margin-bottom:6px;">
        During ANY dispute — Alex's current placement and services CANNOT change</div>
    <div style="color:#7F1D1D;font-size:0.87rem;line-height:1.75;">
        The Stay Put rule means that while a dispute is pending — whether mediation, state complaint, 
        or due process — Alex continues receiving his current IEP services in his current placement. 
        The school cannot remove services or move Alex to a more restrictive setting while a dispute is active.
        This is one of the most important parent protections in IDEA.
    </div>
</div>
""", unsafe_allow_html=True)
law_badge("IDEA § 300.518", "During the pendency of any proceedings, the child must remain in their current educational placement.")

role_tip({
    "Parent / Caregiver": "For the missed speech sessions — file a state complaint. It is free, requires no lawyer, and the state will investigate within 60 days. Document every missed session with dates. For the placement dispute — request mediation first. It preserves your relationship with the school.",
    "Special Education Teacher": "Avoid disputes by documenting everything. If you cannot provide a session, document why and reschedule immediately. A parent who sees consistent make-up scheduling is much less likely to file a complaint.",
    "CSE Coordinator / Administrator": "When a parent disagrees at the IEP meeting, document their objection in writing. Offer mediation proactively. The earlier you address disagreements, the less likely they escalate to due process.",
    "General Education Teacher": "If a parent tells you they are filing a complaint, notify your administrator immediately. Do not make any changes to the student's program without written authorization from the CSE.",
}.get(get_role(), "Four free dispute options. Start with state complaint for violations, mediation for disagreements."))

st.markdown("## 🔀 Final Decision Point")
scenario_box("Alex's parents file a state complaint about the 12 missed speech sessions. The state investigates and confirms the violation. What should happen next?")
choice = st.radio("What should the state order?", [
    "A) The school must apologize in writing",
    "B) The school must provide 12 compensatory speech sessions and prevent future violations",
    "C) Alex must be reevaluated",
    "D) The school's SLP must be replaced",
], label_visibility="collapsed", key="s10_branch")
if choice:
    if choice.startswith("B"):
        st.success("✅ Correct! When a state complaint confirms missed services, the standard remedy is compensatory education — the school must provide the missed sessions on top of regular services. The state may also require a corrective action plan to prevent future violations.")
    elif choice.startswith("A"):
        st.error("❌ An apology is not a legal remedy. Compensatory services — making up what was missed — is the standard required outcome.")
    elif choice.startswith("C"):
        st.error("❌ A reevaluation is not the remedy for missed services. The remedy is compensatory education — providing the missed sessions.")
    else:
        st.error("❌ Personnel decisions are not typically part of a state complaint remedy. The focus is on what the student is owed — compensatory services.")

st.markdown("---")
st.markdown("## 📝 Knowledge Check")
render_quiz(10, [
    {"q": "Alex has missed 12 speech sessions. Which dispute option is BEST to address this?",
     "options": [
         "Due Process — most powerful option",
         "Mediation — voluntary and fast",
         "State Complaint — free investigation of a specific violation",
         "Court — only option that really works",
     ], "correct": 2,
     "explanation": "Missed mandated services are a clear IDEA violation — exactly what state complaints are designed to address. Free, no lawyer needed, 60-day investigation.",
     "wrong_msg": "State complaints are the best fit for clear procedural violations like missed services. Due process is better for complex disputes about the IEP content itself."},
    {"q": "During mediation about placement, can the school move Alex to a more restrictive setting?",
     "options": [
         "Yes — if they have educational justification",
         "No — the Stay Put rule requires Alex to remain in his current placement",
         "Only if the parent agrees",
         "Only if the IEP team votes",
     ], "correct": 1,
     "explanation": "Stay Put is absolute during any pending proceeding. No placement changes without parental consent while a dispute is active.",
     "wrong_msg": "Stay Put means the current placement is frozen during disputes. This is one of the strongest parent protections in IDEA."},
    {"q": "A parent files a state complaint. Can they ALSO request mediation at the same time?",
     "options": [
         "No — choosing one option means giving up the others",
         "Yes — dispute options can be used simultaneously or in sequence",
         "Only if the state approves",
         "Only if the complaint has not been investigated yet",
     ], "correct": 1,
     "explanation": "IDEA dispute options are not mutually exclusive. A parent can file a state complaint, pursue mediation, and file for due process at the same time if they choose.",
     "wrong_msg": "All four dispute options can be used independently or simultaneously. Using one does not waive any other."},
])
