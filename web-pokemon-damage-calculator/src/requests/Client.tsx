import axios from 'axios';
import { SelectedMovesProps, SelectedPokemonProps } from '../components/Selectors';

export const getPokemonNames = (setPokemonNames: (names: string[]) => void, setSelectedPokemon: (name: any) => void) => {
  axios.get('http://0.0.0.0:8000/pokemon-names/')
  .then(response => {
    setPokemonNames(response.data);
    setSelectedPokemon({"left": response.data[0], "right": response.data[0]});
  })
  .catch(error => {
    console.log(error);
  })
}
export const getPokemon = () => {
  axios.get('http://0.0.0.0:8000/pokemon/')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  })
}
export const getMoveNames = (setMoveNames: (moves: string[]) => void, setSelectedMoves: (move: any) => void) => {
  axios.get('http://0.0.0.0:8000/moves/')
    .then(response => {
      setMoveNames(response.data);
      setSelectedMoves({"left": response.data[0], "right": response.data[0]});
    })
    .catch(error => {
      console.log(error);
    })
}
export const DoBattle = async (selectedPokemon: SelectedPokemonProps, selectedMoves: SelectedMovesProps, setBattleResult: (data: any) => void) => {
  const pokemon1 = {
    pokemon_name: selectedPokemon.left,
    move_name: selectedMoves.left,
    evs: {},
    ivs: {},
    level: 100,
  }
  const pokemon2 = {
    pokemon_name: selectedPokemon.right,
    move_name: selectedMoves.right,
    evs: {},
    ivs: {},
    level: 100,
  }
  const body1 = {attacking: pokemon1, defending: pokemon2}
  const body2 = {attacking: pokemon2, defending: pokemon1}
  const left_result = await axios.post('http://0.0.0.0:8000/battle', body1)
    .then(response => {
      return response.data;
    })
    .catch(error => {
      console.log(error);
    })
    const right_result = await axios.post('http://0.0.0.0:8000/battle', body2)
    .then(response => {
      return response.data;
    })
    .catch(error => {
      console.log(error);
    })
  setBattleResult({"left": left_result, "right": right_result});
}
