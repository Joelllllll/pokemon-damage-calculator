import styled from '@emotion/styled';

const StyledTitle = styled("div")`
  color: black;
  font-size: 50px;
  grid-area: header;
  background-color: green;
`;

export const Title = () => {
  return (
    <StyledTitle>
      Pokemon Damage Calculator
    </StyledTitle>
  )
}
