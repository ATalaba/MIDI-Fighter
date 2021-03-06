function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("sound", ev.target.id);
    ev.dataTransfer.setData("name", ev.target.innerHTML);
}

function drop(ev) {
    ev.preventDefault();
    var soundId = ev.dataTransfer.getData("sound");
    var name = ev.dataTransfer.getData("name");

    ev.target.parentElement.setAttribute("data-sound", soundId);
    ev.target.innerHTML = name;
}