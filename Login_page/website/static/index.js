function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
   }).then((_res) => {
        window.location.href = "/";
   });
}

var popup;
function genPassword(){
     popup = window.open("/popup", "Popup", "width=500,height=500");
     popup.focus();
}

usePassword = document.getElementById('use_password');
usePassword.addEventListener('click', () => {
     setPassword();
});

function setPassword(){
     if (window.opener != null && !window.opener.closed){
          passwordField = window.opener.document.getElementById("password1");
          passwordField.value = document.getElementById("passcode").value;
          
          
          // urlParams = new URLSearchParams(window.location.search);
          // password = urlParams.get('password');
          // if (password){
          //      passwordField.value = password;
          // }
     }
     close();
}