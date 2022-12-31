window.onload = function () {
    const urlParams = new URLSearchParams(window.location.search);
    const gameId = urlParams.get("game-id");
    const playerName = urlParams.get("player-name");
    document.getElementById("game-id").value = gameId;
    document.getElementById("player-name").value = playerName;
   }
const host = window.location.protocol + "//" + window.location.host;
const url = host + "/create-game";

window.onload = function () {
    const createGameForm = document.getElementById("create-game-form");
    if (createGameForm != null) {
        createGameForm.addEventListener("submit", create_game);
    }
};
async function create_game(event) {
    event.preventDefault();
    console.log("start request")
    const form = event.currentTarget;
    const formData = new FormData(form);

    const plainFormData = Object.fromEntries(formData.entries());
    const formDataJsonString = JSON.stringify(plainFormData);

    const response = await postData(url, formDataJsonString)

    const resultCreateGame = document.getElementById("create-game-result");
    let h1 = document.createElement('H1');
    resultCreateGame.appendChild(h1)
    if (!response.ok) {
        asynchrone
        const error = await response.json();
        console.log(error)
        h1.innerHTML = "Erreur: " + error.message;
        h1.className = "error";
    } else {
        const gameId = await response.json();
        h1.innerHTML = "Partie créée avec l'id : " + gameId + "<br>";

        let linkToVessels = document.createElement("a");
        const playerName = document.getElementById("player-name").value;
        linkToVessels.href = "manage_fleet.html?game-id=" + gameId + "&player-name=" +
            playerName;
        linkToVessels.text = "Créer votre flotte !"
        h1.appendChild(linkToVessels);
        h1.className = "success";
    }

    event.currentTarget;
    const createGameForm = document.getElementById("create-game-form");
    createGameForm.style.visibility = "hidden";
    resultCreateGame.style.visibility = "visible";
}

async function postData(url = '', data) {
    const fetchOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        body: data,
    };
    return fetch(url, fetchOptions);
}