import { useState } from 'react';
import { useEffect } from 'react';
import './App.css';
import styled from '@emotion/styled';
import { BattleResults } from './components/BattleResults';
import { CombinedMoveSelect, CombinedPokemonSelect, SelectedMovesProps, SelectedPokemonProps, Side } from './components/Selectors';
import { Title } from './components/Title';
import { BattleButton } from './components/BattleButton';
import { DoBattle, getMoveNames, getPokemon, getPokemonNames } from './requests/Client';
import { StatsTable } from './components/Table';


const AppContainer = styled("div")`
  background-color: green;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 0.2fr 0.6fr 1fr 0.4fr 0.3fr 0.4fr;
  grid-template-areas: 
    "header header"
    "pokemon-left pokemon-right"
    "evs-left evs-right"
    "move-left move-right"
    "battle battle"
    "footer footer";
  min-height: 100vh;
  height: 100%;
  width: 100%;
`;

interface StatsSidesProps {
  left: StatsProps;
  right: StatsProps;
}

interface StatsProps {
  ivs: StatsTableProps;
  evs: StatsTableProps;
}

interface StatsTableProps {
  hp: number;
  atk: number;
  def: number;
  spa: number;
  spd: number;
  spe: number;
}

interface Pokemon {
  name: string;
  stats: StatsProps;
}

function App() {
  const [pokemonNames, setPokemonNames] = useState<string[]>([]);
  const [moveNames, setMoveNames] = useState<string[]>([]);
  const [selectedPokemon, setSelectedPokemon] = useState<{left: string, right: string}>({left: "", right: ""});
  const [selectedMoves, setSelectedMoves] = useState<{left: string, right: string}>({left: "", right: ""});
  const [battleResult, setBattleResult] = useState({left: {max: 0, min: 0}, right: {max: 0, min: 0}});
  const [statsSides, setStatSides] = useState({});
  //TODO make a onChange for the inputs in the Table.tsx file

  const handlePokemonSelection = (pokemonName: string, side: string) => {
    if (side == Side.Left) {
      setSelectedPokemon({left: pokemonName, right: selectedPokemon.right});
    }
    else {
      setSelectedPokemon({left: selectedPokemon.left, right: pokemonName});
    }
  }
  const handleMoveSelection = (moveName: string, side: string) => {
    if (side == Side.Left) {
      setSelectedMoves({left: moveName, right: selectedMoves.right});
    }
    else {
      setSelectedMoves({left: selectedMoves.left, right: moveName});
    }
  }
  const SumbitBattle = (selectedPokemon: SelectedPokemonProps, selectedMoves: SelectedMovesProps) => {
    DoBattle(selectedPokemon, selectedMoves, setBattleResult);
    {console.log(getPokemon())}
  }
  useEffect(() => {
    getPokemonNames(setPokemonNames, setSelectedPokemon);
    getMoveNames(setMoveNames, setSelectedMoves);

    }, []
  )
  return (
    <div className="App">
      <AppContainer>
        <Title />
          <CombinedPokemonSelect
            pokemonNames={pokemonNames}
            selectedPokemon={selectedPokemon}
            onChange={handlePokemonSelection}
          />
          <CombinedMoveSelect
            moveNames={moveNames}
            selectedMoves={selectedMoves}
            onChange={handleMoveSelection}
          />
          <StatsTable left={true}/>
          <StatsTable left={false}/>
          <BattleButton 
            selectedPokemon={selectedPokemon}
            selectedMoves={selectedMoves}
            onClick={SumbitBattle}
          />
          <BattleResults left={battleResult.left} right={battleResult.right}/>
      </AppContainer>
    </div>
  );
}

export default App;
