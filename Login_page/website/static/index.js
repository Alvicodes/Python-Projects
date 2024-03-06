function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

var popup;
function genPassword() {
  popup = window.open("/popup", "Popup", "width=800,height=600");
  popup.focus();
}

//! // Copy to clipboard
//  const clipboard = document.querySelector('.clipboard');
//  clipboard.addEventListener('click', () =>{
//      console.log("object copied to clipboard");
//  });

// const passwordField = window.opener.document.getElementById("password1");
// const passwordField2 = window.opener.document.getElementById("password2");
// const usePassword = document.getElementById('use_password');
// const generatedPassword = document.getElementById('generatedPassword');
// usePassword.addEventListener('click', () => {
//      setPassword();
// });

//! // Set Password
// function setPassword(){
//      if (window.opener != null && !window.opener.closed){
//           const passwordText = generatedPassword.textContent;
//           passwordField.value = passwordText;
//           passwordField2.value = passwordText;

//      }
//      window.close();
// };

const clrSelect = document.querySelectorAll(".note-clr");
const note_Background = document.querySelector(".note-pad");
// const uniqueNoteId = document.querySelector()
// const clr_Pink = document.getElementById('clr-pink');
// const clr_Orange = document.getElementById('clr-orange');
// const clr_Yellow = document.getElementById('clr-yellow');
// const clr_lightblue = document.getElementById('clr-lightblue');
// const clr_Blue = document.getElementById('clr-blue');

clrSelect.forEach((item) => {
  item.addEventListener("click", () => {
    // const clrClass = item.classList[2];
    // const uniqueNoteId = noteBackgrounds[index];
    var colorClass = item.classList[1];
    var parentNote = item.closest('.note-pad');
    if (parentNote && colorClass) {
      if (parentNote.classList.contains(colorClass)) {
        parentNote.classList.remove(colorClass);
      }
      else {
        var existingColorClass = parentNote.classList.value.match(/clr-\w+/);// Regular expression to match "clr-" followed by any word characters
        if (existingColorClass) {
          parentNote.classList.remove(existingColorClass);
        }
        parentNote.classList.add(colorClass);
      }
    }
    });
});

//! Generate random code for each note
// attach to li onclick
//
