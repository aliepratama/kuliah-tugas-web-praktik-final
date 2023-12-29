import { ref, query, limitToLast, limitToFirst, get, child, remove } from "firebase/database";
import { database } from "../firebase";

const db = ref(database, '/history');

class HistoryDatabaseService {
    static async getAllData(uid, limit=20, order='desc') {
        if(limit >= 0){
            if(order === 'desc'){
                const data = await get(query(child(db, `/${uid}`), limitToLast(limit)));
                return data.val();
            }
            const data = await get(query(child(db, `/${uid}`), limitToFirst(limit)));
            return data.val();
        }
    }
    static async removeData(uid, node) {
        remove(ref(database, `/history/${uid}/${node}`));
    }
}

export { HistoryDatabaseService };
