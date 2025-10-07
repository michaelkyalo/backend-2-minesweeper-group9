import {BrowserRouter, Routes, Route} from "react-router-dom";
import Welcome from "./welcome"
import GameScreen from "./gamescreen"
import "../index.css"

function MineSweeper(){
    return (
        <BrowserRouter className="app-container">
            <h1 className="app-header">MINI MINESWEEPER</h1>
            <Routes>
                <Route path="/" element={<Welcome />}/>
                <Route path="/play" element={<GameScreen />}/>
            </Routes>
        </BrowserRouter>
    );
};

export default MineSweeper;
