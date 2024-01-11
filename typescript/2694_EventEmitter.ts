// Problem 2694: Event Emitter
// https://leetcode.com/problems/event-emitter/

type Callback = (...args: any[]) => any;
type Subscription = {
  unsubscribe: () => void
}

class EventEmitter {
  // 先宣告一個私有的map, 儲存事件 和 它的callback function array
  private eventNames: Map<string, Callback[]> = new Map();

  // 訂閱事件
  subscribe(eventName: string, callback: Callback): Subscription {
    // 如果目前的map裡面沒有這個事件, 就新增, 預設空陣列
    if (!this.eventNames.has(eventName)) {
      this.eventNames.set(eventName, []);
    }

    // 取得這個事件的callback並新增一個新的element
    const listeners = this.eventNames.get(eventName)!;
    listeners.push(callback);

    return {
      unsubscribe: () => {
        // 尋找被取消的callback, index 不等於 -1 即為有找到, 則刪除它
        const index = listeners.indexOf(callback);
        if (index !== -1) {
          listeners.splice(index, 1);
        }
      }
    };
  }

  // 觸發事件
  emit(eventName: string, args: any[] = []): any[] {
    // 如果目前的map裡面沒有這個事件, 就回傳空陣列
    if (!this.eventNames.has(eventName)) {
      return [];
    }

    // 取得這個事件的callback並用迴圈執行
    const listeners = this.eventNames.get(eventName)!;
    const results: any[] = [];

    for (const listener of listeners) {
      results.push(listener(...args));
    }

    return results;
  }
}