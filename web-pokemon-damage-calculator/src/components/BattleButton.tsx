import styled from '@emotion/styled';
import { SelectedMovesProps, SelectedPokemonProps } from './Selectors';

const StyledBattleButton = styled("button")`
  grid-area: battle;
  background-color: yellow;
  height: 100%;
`

interface BattleButtonProps {
  selectedPokemon: SelectedPokemonProps;
  selectedMoves: SelectedMovesProps;
  onClick: (selectedPokemon: SelectedPokemonProps, selectedMoves: SelectedMovesProps) => void;
}

export const BattleButton = ({selectedPokemon, selectedMoves, onClick}: BattleButtonProps) => {
  return(
    <StyledBattleButton onClick={() => onClick(selectedPokemon, selectedMoves)}>
      <h2>
        Battle!
      </h2>
    </StyledBattleButton>
  )
}
