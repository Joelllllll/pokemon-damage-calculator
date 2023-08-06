import styled from '@emotion/styled';
import { Select, MenuItem} from '@mui/material';


const StyledSelect = styled(Select)<{left: any, grid: any}>`
  grid-area: ${props => props.grid}-${props => props.left ? Side.Left : Side.Right};
  background-color: ${props => props.left ? "red" : "blue"};
  height: 100%;
`

export enum Side {
  Left = "left",
  Right = "right"
}

export interface SelectedPokemonProps {
  left: string;
  right: string;
}

interface CombinedPokemonSelectProps {
  pokemonNames: string[];
  selectedPokemon: SelectedPokemonProps;
  onChange: (pokemonName: string, side: string) => void;
}

export const CombinedPokemonSelect = ({pokemonNames, selectedPokemon, onChange}: CombinedPokemonSelectProps) => {
  return (
    <>
      <StyledSelect left={true? 1: 0} value={selectedPokemon.left} grid={"pokemon"}>
        {pokemonNames.map((pokemonName: string) => (
          <MenuItem
            key={pokemonName}
            onClick={() => onChange(pokemonName, Side.Left)}
            value={pokemonName}>
              {pokemonName}
          </MenuItem>
        ))}
      </StyledSelect>
      <StyledSelect left={false? 1: 0} value={selectedPokemon.right} grid={"pokemon"}>
      {pokemonNames.map((pokemonName: string) => (
          <MenuItem
            key={pokemonName}
            onClick={() => onChange(pokemonName, Side.Right)}
            value={pokemonName}>
              {pokemonName}
            </MenuItem>
        ))}
      </StyledSelect>
    </>
  )
}

export interface SelectedMovesProps {
  left: string;
  right: string;
}

interface CombinedMoveSelectProps {
  moveNames: string[];
  selectedMoves: SelectedMovesProps;
  onChange: (moveName: string, side: string) => void;
}

export const CombinedMoveSelect = ({moveNames, selectedMoves, onChange}: CombinedMoveSelectProps) => {
  return (
    <>
      <StyledSelect left={true? 1: 0} value={selectedMoves.left} grid={"move"}>
        {moveNames.map((moveName: string) => (
          <MenuItem
            key={moveName}
            onClick={() => onChange(moveName, Side.Left)}
            value={moveName}>
              {moveName}
          </MenuItem>
        ))}
      </StyledSelect>
      <StyledSelect left={false? 1: 0} value={selectedMoves.right} grid={"move"}>
      {moveNames.map((moveName: string) => (
          <MenuItem
            key={moveName}
            onClick={() => onChange(moveName, Side.Right)}
            value={moveName}>
              {moveName}
          </MenuItem>
        ))}
      </StyledSelect>
    </>
  )
}
