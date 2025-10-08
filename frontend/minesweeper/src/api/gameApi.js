import axios from "axios";
import API_BASE_URL from "../config";

export const createGame = async (rows, cols, mines) => {
  const res = await axios.post(`${API_BASE_URL}/games/`, { rows, cols, mines });
  return res.data;
};

export const revealCell = async (gameId, row, col) => {
  const res = await axios.post(`${API_BASE_URL}/games/${gameId}/reveal`, { row, col });
  return res.data;
};
