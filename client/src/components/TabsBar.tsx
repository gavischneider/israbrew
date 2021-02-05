import { useEffect, useState } from "react";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import "react-tabs/style/react-tabs.css";
import { BeersJSON } from "../types/BeersJSON";
import { BeerGrid } from "./BeerGrid";

export const TabsBar = () => {
  const initialState = {
    beerandbeyond: [],
    biratenu: [],
    mendelson: [],
    beerz: [],
  };
  const [beers, setBeers] = useState<BeersJSON>(initialState);

  useEffect(() => {
    fetch("/api/beer")
      .then((res) => res.json())
      .then((data) => {
        setBeers(data.beers);
      });
  }, []);

  return (
    <Tabs>
      <TabList>
        <Tab>Home</Tab>
        <Tab>Beer And Beyond</Tab>
        <Tab>Biratenu</Tab>
        <Tab>Mendelson Heshin</Tab>
        <Tab>BeerZ</Tab>
        <Tab>Toad</Tab>
      </TabList>

      <TabPanel>
        <h1>Home</h1>
      </TabPanel>

      <TabPanel>
        <BeerGrid beers={beers.beerandbeyond} />
      </TabPanel>
      <TabPanel>
        <BeerGrid beers={beers.biratenu} />
      </TabPanel>
      <TabPanel>
        <BeerGrid beers={beers.mendelson} />
      </TabPanel>
      <TabPanel>
        <BeerGrid beers={beers.beerz} />
      </TabPanel>
      <TabPanel>
        <p>
          <b>Toad</b> (<i>Japanese: キノピオ Hepburn: Kinopio</i>) is a
          fictional character who primarily appears in Nintendo's Mario
          franchise. Created by Japanese video game designer Shigeru Miyamoto,
          he is portrayed as a citizen of the Mushroom Kingdom and is one of
          Princess Peach's most loyal attendants; constantly working on her
          behalf. He is usually seen as a non-player character (NPC) who
          provides assistance to Mario and his friends in most games, but there
          are times when Toad(s) takes center stage and appears as a
          protagonist, as seen in Super Mario Bros. 2, Wario's Woods, Super
          Mario 3D World, and Captain Toad: Treasure Tracker.
        </p>
        <p>
          Source:{" "}
          <a
            href="https://en.wikipedia.org/wiki/Toad_(Nintendo)"
            target="_blank"
            rel="noreferrer"
          >
            Wikipedia
          </a>
        </p>
      </TabPanel>
    </Tabs>
  );
};
