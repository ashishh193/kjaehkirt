import streamlit as st

st.title("Todo List App")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add new task
new_task = st.text_input("Add a new task")
if st.button("Add Task") and new_task:
    st.session_state.tasks.append({"task": new_task, "done": False})
    st.experimental_rerun()

# Display tasks
st.subheader("Tasks")
for idx, item in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([8, 1])
    with col1:
        st.write(f"{item['task']}" if not item["done"] else f"~~{item['task']}~~")
    with col2:
        if not item["done"]:
            if st.button("Done", key=f"done_{idx}"):
                st.session_state.tasks[idx]["done"] = True
                st.experimental_rerun()
