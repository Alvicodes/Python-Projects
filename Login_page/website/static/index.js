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
     popup = window.open("Popup.html", "Popup", "width=300, height=300");
     popup.focus();
}