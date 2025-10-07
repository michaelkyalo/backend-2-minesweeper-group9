import {useNavigate} from "react-router";

function Welcome(){
    const navigate = useNavigate();
    return(
        <div className="app-container">
            <div className="welcome-box">
            <h2>Welcome to Minesweeper.</h2>
                <div className="instructions">
                    <p>Instructions:</p>
                    <ol>
                        <li>Click to reveal a cell.</li>
                        <li>Right-click to place a flag.</li>
                        <li>Reveal all safe cells to win.</li>
                        <li>Avoid the mines!</li>
                    </ol>
                </div>
            </div>
            <button className="start-btn" onClick={()=>{navigate("/play")}}>START GAME.</button>
        </div>
    );
};

export default Welcome;
