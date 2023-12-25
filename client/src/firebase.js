import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";

const firebaseConfig = {
    // apiKey: "AIzaSyB8BO-nwXjiCARG-LBxMQFQ08TgaTGn7Mk",
    // authDomain: "zimo-tools.firebaseapp.com",
    databaseURL: "https://zimo-tools-default-rtdb.asia-southeast1.firebasedatabase.app",
    // projectId: "zimo-tools",
    // storageBucket: "zimo-tools.appspot.com",
    // messagingSenderId: "874018918469",
    // appId: "1:874018918469:web:54516b1eaaf64db126d32c",
    // measurementId: "G-ZVW8EVDDEE"
  };

const app = initializeApp(firebaseConfig);

export const database = getDatabase(app);
