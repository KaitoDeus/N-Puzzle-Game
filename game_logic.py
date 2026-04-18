import random

class PuzzleGame:
    def __init__(self, size=3):
        self.size = size
        self.goal_state = list(range(1, size * size)) + [0]
        self.current_state = list(self.goal_state)
        self.history = []
        self.redo_stack = []
        self.shuffle()

    def is_solvable(self, state):
        inversions = 0
        arr = [x for x in state if x != 0]
        # Đếm số cặp nghịch thế (số lớn đứng trước số nhỏ)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    inversions += 1
        # Trạng thái có thể giải được nếu số cặp nghịch thế là số chẵn
        return inversions % 2 == 0

    def shuffle(self):
        state = list(self.goal_state)
        while True:
            random.shuffle(state)
            if self.is_solvable(state) and state != self.goal_state:
                break
        self.current_state = state
        self.history = []
        self.redo_stack = []

    def get_empty_pos(self):
        idx = self.current_state.index(0)
        return idx // self.size, idx % self.size

    def move(self, tile_index, record_history=True):
        """Cố gắng di chuyển một ô nếu nó nằm sát cạnh ô trống."""
        empty_idx = self.current_state.index(0)
        
        r_empty, c_empty = empty_idx // self.size, empty_idx % self.size
        r_tile, c_tile = tile_index // self.size, tile_index % self.size
        
        # Chỉ kề nhau khi hoảng cách Manhattan bằng 1
        if abs(r_empty - r_tile) + abs(c_empty - c_tile) == 1:
            if record_history:
                self.history.append(list(self.current_state))
                self.redo_stack.clear()

            self.current_state[empty_idx], self.current_state[tile_index] = \
                self.current_state[tile_index], self.current_state[empty_idx]
            return True
        return False

    def undo(self):
        if self.history:
            self.redo_stack.append(list(self.current_state))
            self.current_state = self.history.pop()
            return True
        return False

    def redo(self):
        if self.redo_stack:
            self.history.append(list(self.current_state))
            self.current_state = self.redo_stack.pop()
            return True
        return False

    def is_goal(self):
        return self.current_state == self.goal_state

    def reset(self):
        self.shuffle()
