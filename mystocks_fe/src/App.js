import React, { useState, Component, Fragment } from "react";
import Header from "./scenes/global/Header";
import Home from "./components/Home";
import { ColorModeContext, useMode } from "./theme";
import { Routes, Route } from "react-router-dom";
import { CssBaseline, ThemeProvider } from "@mui/material";

function App() {

  const [theme, colorMode] = useMode();
  const [isSidebar, setIsSidebar] = useState(true);

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          <main className="content">
            <Header setIsSidebar={setIsSidebar} /> 
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
