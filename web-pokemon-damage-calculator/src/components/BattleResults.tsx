import styled from '@emotion/styled';

const StyledBattleResults = styled("div")<{left: any}>`
  grid-area: footer;
  background-color: orange;
  grid-column: ${props => props.left ? 1 : 2};
  height: 100%
`

interface BattleResultProps {
  left: any;
  right: any;
}

export const BattleResults = ({left, right}: BattleResultProps) => {
  return (
    <>
      <StyledBattleResults left={false}>
        <h2>
          {"max: " + right.max + "%"}
          <br></br>
          {"min: " + right.min + "%"}
        </h2>
      </StyledBattleResults>
      <StyledBattleResults left={true}>
        <h2>
          {"max: " + left.max + "%"}
          <br></br>
          {"min: " + left.min + "%"}
        </h2>
      </StyledBattleResults>
    </>
  )
}
