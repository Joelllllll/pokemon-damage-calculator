import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import styled from '@emotion/styled';
import { Side } from './Selectors';

const Stats = ["HP", "Attack", "Defense", "Special Attack", "Special Defense", "Speed"]

const StyledTable = styled("div")<{left: boolean}>`
    grid-area: evs-${props => props.left ? Side.Left : Side.Right};
    height: 100%;
`
interface EvsProps {
    left: boolean;
}
export const StatsTable = ({left}: EvsProps) => {
  return (
    <StyledTable left={left}>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell align="right"><b></b></TableCell>
              <TableCell align="right"><b>Base</b></TableCell>
              <TableCell align="right"><b>IVs</b></TableCell>
              <TableCell align="right"><b>Evs</b></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {Stats.map((stat: string) => (
              <TableRow
                key={stat}
              >
              <TableCell component="th" scope="row">
              <b>{stat}</b>
              </TableCell>
              <TableCell align="right"><input defaultValue={0}/></TableCell>
              <TableCell align="right"><input defaultValue={31}/></TableCell>
              <TableCell align="right"><input defaultValue={0}/></TableCell>
        </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </StyledTable>
  );
}