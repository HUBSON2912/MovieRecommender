import { createTheme } from '@mui/material/styles';

export const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#de4343',
    },
    secondary: {
      main: '#43DEDE',
    },
    text: {
      primary: '#ffffff',
    },
    background: {
      paper: '#3a3939',
    },
  },
  shape: {
    borderRadius: 5,
  },
  typography: {
    fontFamily: 'Slabo 27px',
    fontSize: 24
  },
});