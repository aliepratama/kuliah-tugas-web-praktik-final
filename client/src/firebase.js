import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";

const firebaseConfig = {
    databaseURL: "https://zimo-tools-default-rtdb.asia-southeast1.firebasedatabase.app",
  };

const app = initializeApp(firebaseConfig);

export const database = getDatabase(app);
