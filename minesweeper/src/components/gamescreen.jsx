import TopBar from "./gamescreen/topbar"
// import Board from "./gamescreen/board"


function GameScreen(){
    return(
        <div>
            <div className="game-box">
                <h2>Game box</h2>
                <TopBar />
                {/* <Board /> */}
            </div>
        </div>
    );
};

export default GameScreen;