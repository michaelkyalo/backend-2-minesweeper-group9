import React from 'react';

const Cell = ({ cell, handleCellClick, row, col }) => {
  return (
    <div
      className={`cell ${cell.revealed ? 'revealed' : ''} ${cell.mine ? 'mine' : ''}`}
      onClick={() => handleCellClick(row, col)}
    >
      {cell.revealed ? (cell.mine ? 'X' : cell.adjacentMines || '') : ''}
    </div>
  );
};

export default Cell;