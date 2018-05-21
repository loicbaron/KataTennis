document.getElementById('gameInputForm').addEventListener('submit', performPostGame);

function performPostGame(e) {

    var playerOne = document.getElementById('playerOne').value;
    var playerTwo = document.getElementById('playerTwo').value;

    axios.post('/api/games', {
        playerOne: playerOne,
        playerTwo: playerTwo
    })
        .then(function (response) {
            console.log(response);
            window.location.replace("/games/"+response.data.game[0].id);
        })
        .catch(function (error) {
            console.log(error);
        });

    e.preventDefault();
}
