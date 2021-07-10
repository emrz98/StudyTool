import React from 'react'
import { useEffect, useState } from "react";
import { makeStyles } from '@material-ui/core/styles';
import Fab from '@material-ui/core/Fab';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import axios from 'axios';
import AddIcon from '@material-ui/icons/Add';

const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
    },
    paper: {
      padding: theme.spacing(2),
      textAlign: 'center',
      color: 'black',
    },
    title:{
        textAlign:'center',
        color:'blue'
    },
    tableDecks:{
        display:'block-inline'
    }
  }));

function MainMenu(props){
    const classes = useStyles();
    const [decks, setDecks] = useState([]);

    useEffect(() => {
        const getDecks = () => {
            axios.get('decks/')
            .then(response => {
                setDecks(response.data)
            }).catch(e => alert(e));
        }
        getDecks();
    },[]);

    const handleAddDeck = () =>{
        

    }

    return(
    <>
    <Grid container spacing={3}>
        <Grid item xs={12}>
          <h1 className={classes.title}>My Tool of study</h1>
        </Grid>
        <Grid item xs={12}>
          <Paper className={classes.paper}>
            <h3>Decks List</h3>
            <table>
              <tr>
              {decks.map((deck) => (
                  <>
                  <td>{deck.name}</td>
                  <td>1</td>
                  </>
              ))}
              </tr>
            </table>
            <Fab color="primary" aria-label="add" onClick={e => handleAddDeck(e)}>
              <AddIcon />
            </Fab>
          </Paper>
        </Grid>
      </Grid>
      </>
    );

}

export default MainMenu;