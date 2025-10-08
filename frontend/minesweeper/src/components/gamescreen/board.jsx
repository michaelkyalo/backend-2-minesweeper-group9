import React from 'react';
import Cell from './cell';
import { createGame, revealCell } from "../api/gameApi";
const Board = ({ grid, handleCellClick }) => {
  return (
    <div className="board">
      {grid?.map((row, rowIndex) => (
        <div key={rowIndex} className="row">
          {row.map((cell, colIndex) => (
            <Cell
              key={colIndex}
              cell={cell}
              handleCellClick={handleCellClick}
              row={rowIndex}
              col={colIndex}
            />
          ))}
        </div>
      ))}
    </div>
  );
};

export default Board;