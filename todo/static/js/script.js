
// Set footer year
document.addEventListener("DOMContentLoaded", () => {
  const y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
});


//Toast Function
function showToast(status,message){
  let toast = document.getElementById("toast");  
  toast.innerHTML = message
  newClassName=`show-${status}`
  toast.className = `show-${status}`
  setTimeout(()=>{
    toast.className=toast.className.replace(newClassName,"");
    toast.innerHTML=""
  },3000)
}



// Mobile nav toggle
const toggle = document.querySelector(".nav-toggle");
const nav = document.querySelector(".site-nav");

  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }


// Model Add Task
const openAddBtn = document.getElementById('addOpenModal');
const closeAddBtn = document.getElementById('addCloseModal');
const modalAdd = document.getElementById('addTaskModal');



openAddBtn.addEventListener('click',()=>{
  modalAdd.style.display = 'flex';
})

closeAddBtn.addEventListener('click', () => {
  modalAdd.style.display = 'none';
});
window.addEventListener('click',(e)=>{
  if (e.target == modalAdd){
    modalAdd.style.display = 'none';
  }if (e.target == updateModal){
    updateModal.style.display = 'none';
  }
})


// Create Task
document.getElementById('addTaskForm').addEventListener('submit',(e)=>{
  e.preventDefault();
  let formData = new FormData(e.target);
  fetch("task_create",{
    method:'POST',
    headers: {
      "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
      },
    body: formData
  })
  .then(res=>res.json())
  .then(data=>{
    if (data.status=="success"){
      modalAdd.style.display = 'none';
      showToast("success","Added Successfully")
      setTimeout(()=> location.reload() , 1000);
    }

    else {
      let errors = data.errors;
      let messages = [];
  
      for (let field in errors) {
        if (errors.hasOwnProperty(field)) {
          errors[field].forEach(msg => {
            messages.push(`${field}: ${msg}`);
          });
        }
      }
      showToast("error", messages.join("\n"));
    }
  })
  .catch(error => showToast("error",error));
  
})

//Edit task
const updateButtons = document.querySelectorAll(".btn-update");
const updateModal = document.getElementById("updateTaskModal");
const updateClose = document.getElementById("updateCloseModal");
const updateForm = document.getElementById("updateTaskForm");
updateButtons.forEach(btn=>{
btn.addEventListener("click",()=>{
const id = btn.getAttribute('data-id')
const title = btn.getAttribute('data-title')
const description  = btn.getAttribute('data-description')
const complete = btn.getAttribute('data-complete')==="True"

document.getElementById("update_id").value = id
document.getElementById("update_title").value = title
document.getElementById("update_description").value = description
document.getElementById("update_complete").checked = complete

updateModal.style.display = "flex"
})
})
updateCloseModal.addEventListener("click",()=>{
updateModal.style.display = "none";
})


// Submit update form
updateForm.addEventListener("submit", (e) => {
  e.preventDefault();
  let formData = new FormData(e.target);
  let id = formData.get("id");
   console.log(formData)
  fetch(`task_update/${id}`, {
    method: "POST",
    headers: {
      "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
    },
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      if (data.status === "success") {
        updateModal.style.display = "none";
        showToast("success", "Updated Successfully");
        setTimeout(() => location.reload(), 1000);
      } else {
        let errors = data.errors;
        let messages = [];

        for (let field in errors) {
          if (errors.hasOwnProperty(field)) {
            errors[field].forEach(msg => {
              messages.push(`${field}: ${msg}`);
            });
          }
        }
        showToast("error", messages.join("\n"));
      }
    })
    .catch(error => showToast("error", error));
});
