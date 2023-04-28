import logo from "./logo.svg";
import "./App.css";
import { useEffect, useState } from "react";

import Container from "@mui/material/Container";
import Card from "@mui/material/Card";
import Button from "@mui/material/Button";
import AppBar from "@mui/material/AppBar";
import Stack from "@mui/material/Stack";
import { CssBaseline } from "@mui/material";

function IndustryCard(id) {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8000/industries/${id.id}`)
      .then((res) => res.json())
      .then((data) => setData(data));
  }, []);

  return (
    <Card sx={{ margin: 2 }}>
      <b>Industry</b>
      <div>{data?.name}</div>
    </Card>
  );
}

function App() {
  const [favorites, setFavorites] = useState("undefined");
  const [data, setData] = useState(null);

  function load() {
    fetch(`http://localhost:8000/leads/?is_favorite=${favorites}`)
      .then((res) => res.json())
      .then((data) => setData(data));
  }

  function toggleFavorite(lead) {
    fetch(`http://localhost:8000/leads/${lead.id}/`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ...lead, is_favorite: !lead.is_favorite }),
    })
      .then((res) => res.json())
      .then((data) => {
        load();
      });
  }

  useEffect(() => {
    load();
  }, [favorites]);

  return (
    <div className="App">
      <AppBar position="static">Leads</AppBar>

      <Button
        variant="text"
        onClick={() => setFavorites(favorites == "true" ? "undefined" : "true")}
      >
        Showing: {favorites == "true" ? "Favorites" : "All"}
      </Button>

      <Container sx={{ textAlign: "left" }}>
        <CssBaseline />

        <Stack spacing={2}>
          {data?.map((lead) => (
            <Card>
              <h1>{lead.business.name}</h1>

              <Card sx={{ margin: 2 }}>
                <b>About</b>
                <div>{lead.business.description}</div>
              </Card>

              <IndustryCard id={lead.business.industry_id} />

              <Card sx={{ margin: 2 }}>
                <h2>Owner</h2>
                <b>Name</b>
                <div>{lead.business.owner_full_name} </div>
                <b>Profile Image</b>
                <div>
                  <img src={lead.img} height="64" />
                </div>
                <b>About Me</b>
                <div>{lead.business.about_the_owner}</div>
              </Card>

              {lead.is_favorite ? (
                <Button
                  id="favorite-button"
                  sx={{ margin: 2 }}
                  variant="contained"
                  onClick={() => toggleFavorite(lead)}
                >
                  Favorite
                </Button>
              ) : (
                <Button
                  id="unfavorite-button"
                  sx={{ margin: 2 }}
                  variant="contained"
                  onClick={() => toggleFavorite(lead)}
                >
                  Unfavorite
                </Button>
              )}
            </Card>
          ))}
        </Stack>
      </Container>
    </div>
  );
}

export default App;
