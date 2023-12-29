import { ref, query, limitToLast, limitToFirst, get, child } from "firebase/database";
import { database } from "../firebase";

const db = ref(database, '/history');

class HistoryDatabaseService {
    static async getAllData(limit=20, order='desc') {
        if(limit >= 0){
            if(order === 'desc'){
                const data = await get(query(child(db, '/10'), limitToLast(limit)));
                return data.val();
            }
            const data = await get(query(child(db, '/10'), limitToFirst(limit)));
            return data.val();
        }
    }
}

export { HistoryDatabaseService };
