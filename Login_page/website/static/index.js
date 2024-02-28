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

// // Copy to clipboard
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

// function setPassword(){
//      if (window.opener != null && !window.opener.closed){
//           const passwordText = generatedPassword.textContent;
//           passwordField.value = passwordText;
//           passwordField2.value = passwordText;

//      }
//      window.close();
// };

const clr_Selection = document.querySelectorAll(".note-clr");
const note_Background = document.querySelector(".note-pad");
// const clr_Pink = document.getElementById('clr-pink');
// const clr_Orange = document.getElementById('clr-orange');
// const clr_Yellow = document.getElementById('clr-yellow');
// const clr_lightblue = document.getElementById('clr-lightblue');
// const clr_Blue = document.getElementById('clr-blue');

clr_Selection.forEach((item) => {
  item.addEventListener("click", () => {
    const clrClass = item.classList[2];
    const noteBackground = noteBackgrounds[index];
    // Remove all class names that start with 'clr-'
    Array.from(noteBackground.classList).forEach((className) => {
      if (className.startsWith("clr-")) {
        noteBackground.classList.remove(className);
      }
    });
    note_Background.classList.add(clrClass);
  });
});
