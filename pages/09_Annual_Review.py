"""Step 9 — Annual Review"""
import streamlit as st, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
st.set_page_config(page_title="Step 9 · IEP Tutorial", page_icon="🔄", layout="wide")
from utils.engine import *
apply_theme(); init_session(); sidebar_nav()
page_header("🔄", "Step 9 — Annual Review & Reevaluation", "The IEP must be reviewed every year — and fully reevaluated every 3 years")
step_badge(9)

scenario_box("It is now one year later. Alex has made good progress in reading. His resource room teacher has been tracking data weekly. Alex's parents have been receiving quarterly progress reports. The CSE schedules the annual review meeting for May 15th — before the IEP anniversary date of May 25th.")

st.markdown("## The Annual Review Cycle")
for title, desc, color in [
    ("Must happen at least once per year", "The IEP must be reviewed on or before the IEP anniversary date. Missing the annual review is a procedural violation.", "#2563EB"),
    ("Parent must be invited", "Written notice must be sent with enough time for the parent to attend — at least 5 school days.", "#0D9488"),
    ("Progress on goals must be reported", "The team reviews whether Alex met his annual goals. Goals should be measurable so this is clear.", "#7C3AED"),
    ("Goals are updated", "New annual goals are written based on current Present Levels of Performance.", "#D97706"),
    ("Services can be changed", "If Alex has made enough progress, services may be reduced. If he needs more support, services can be increased.", "#16A34A"),
]:
    st.markdown(f"""
    <div style="display:flex;gap:10px;align-items:flex-start;padding:8px 0;border-bottom:1px solid #F1F5F9;">
        <span style="color:{color};font-size:1rem;flex-shrink:0;">▸</span>
        <div><b style="color:#1E293B;font-size:0.87rem;">{title}:</b>
        <span style="color:#475569;font-size:0.87rem;"> {desc}</span></div>
    </div>""", unsafe_allow_html=True)

st.markdown("## The 3-Year Reevaluation")
st.markdown("""
<div style="background:#FFF8E1;border:1px solid #D97706;border-radius:10px;padding:14px 18px;margin:10px 0;">
    <div style="font-weight:700;color:#D97706;margin-bottom:6px;">Triennial Reevaluation — Required Every 3 Years</div>
    <div style="color:#334155;font-size:0.87rem;line-height:1.75;">
        Every 3 years, the school must conduct a full reevaluation to determine whether the student still qualifies 
        and what their current needs are. The parent must consent. The team reviews existing data and determines 
        what new testing is needed (if any). Parents can request a reevaluation sooner if the child's needs change significantly.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("## Amending the IEP Without a Meeting")
st.markdown("""
<div style="background:#EFF6FF;border-left:4px solid #2563EB;border-radius:8px;padding:12px 16px;margin:10px 0;">
    <div style="font-weight:700;color:#1E40AF;margin-bottom:4px;">IEP Amendment — A Shortcut for Small Changes</div>
    <div style="color:#334155;font-size:0.87rem;line-height:1.75;">
        Not every change requires a full meeting. If the parent and school agree, a written amendment 
        can be made to the IEP without convening the full team. This is useful for minor updates — 
        changing service frequency, adding an accommodation, updating a goal mid-year.
        Both parties must agree in writing.
    </div>
</div>
""", unsafe_allow_html=True)

role_tip({
    "Parent / Caregiver": "Before the annual review, request your child's progress data. Review it before the meeting so you come prepared with questions. Ask: Did they meet each goal? If not, why? What is the plan?",
    "Special Education Teacher": "Bring data to the annual review — not just a verbal report. Charts showing progress on measurable goals are much more credible than 'Alex is doing better.'",
    "CSE Coordinator / Administrator": "Track IEP anniversary dates for your entire caseload. Missing even one annual review is a violation. Many districts use automated systems — verify your list monthly.",
    "General Education Teacher": "Annual review is a good time to update the team on classroom performance. If your observations differ from the special ed data, say so — the team needs the full picture.",
}.get(get_role(), "Annual review must happen on or before the IEP anniversary date every year."))

st.markdown("## 🔀 Decision Point — School Misses the Annual Review Date")
scenario_box("Alex's IEP anniversary date is May 25th. It is June 1st and no annual review meeting has been held. The school says they were too busy with end-of-year activities.")
choice = st.radio("What has occurred and what should the parent do?", [
    "A) Nothing — annual reviews can happen anytime in the summer",
    "B) A procedural violation has occurred — parent should put the concern in writing and request an immediate meeting",
    "C) Alex automatically loses services",
    "D) The school has 30 more days before it becomes a violation",
], label_visibility="collapsed", key="s9_branch")
if choice:
    if choice.startswith("B"):
        st.success("✅ Correct! Missing the annual review date is an IDEA procedural violation. The parent should document it in writing, request an immediate meeting, and note that a state complaint may be filed if the school continues to delay.")
    elif choice.startswith("A"):
        st.error("❌ Not correct. The annual review must happen ON OR BEFORE the IEP anniversary date. June 1st — one week past May 25th — is already a violation.")
    elif choice.startswith("C"):
        st.error("❌ Not correct. Alex's current IEP and services remain in effect. However, without an updated IEP, goals cannot be updated and the school's legal obligations become unclear.")
    else:
        st.error("❌ Not correct. There is no 30-day grace period. The anniversary date is the deadline.")

st.markdown("---")
st.markdown("## 📝 Knowledge Check")
render_quiz(9, [
    {"q": "When must the annual IEP review happen?",
     "options": [
         "Within 90 days of the anniversary",
         "On or before the IEP anniversary date",
         "During the last week of school",
         "Whenever the school schedules it",
     ], "correct": 1,
     "explanation": "The annual review must happen on or before the anniversary of the IEP meeting date. There is no grace period — the anniversary date is the hard deadline.",
     "wrong_msg": "The anniversary date is a hard deadline. 'Approximately annually' or 'within the school year' are not correct — it must be on or before the specific date."},
    {"q": "Alex has made dramatic progress and his parents want his services reduced. What is the process?",
     "options": [
         "The school unilaterally reduces services",
         "Services can only be reduced at the 3-year reevaluation",
         "The IEP team — including parents — reviews data and agrees to amend the IEP",
         "A new evaluation must be done first",
     ], "correct": 2,
     "explanation": "Any change to services — increase or decrease — must be agreed to by the IEP team. The parent is an equal member of that decision.",
     "wrong_msg": "Services cannot be changed unilaterally by either party. The IEP team — including the parent — reviews the data and makes the decision together."},
    {"q": "What triggers a reevaluation before the 3-year mark?",
     "options": [
         "Nothing — only the 3-year deadline triggers reevaluation",
         "Parent request OR school determines student's needs have changed significantly",
         "A new teacher requests it",
         "A change in the student's address",
     ], "correct": 1,
     "explanation": "A reevaluation can be requested by the parent at any time OR by the school when it determines the student's educational or related service needs warrant a reevaluation.",
     "wrong_msg": "Both parents and schools can request an early reevaluation when warranted by changes in the student's needs. The 3-year mark is the maximum — not the only trigger."},
])
