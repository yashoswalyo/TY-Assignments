#include <algorithm>
#include <cstdio>
#include <map>
#include <stack>

using namespace std;
// x and y are the amounts of water in litres in the two jugs respectively
struct state {
  int x, y;
  bool operator<(const state &that) const {
    if (x != that.x)
      return x < that.x;
    return y < that.y;
  }
};
int capacity_x, capacity_y, target;
void dfs(state start, stack<pair<state, int>> &path) {
  stack<state> s;
  state goal = (state){-1, -1};
  map<state, pair<state, int>> parentOf;
  s.push(start);
  parentOf[start] = make_pair(start, 0);
  while (!s.empty()) {
    state top = s.top();
    s.pop();
    if (top.x == target || top.y == target) {

      goal = top;
      break;
    }
    if (top.x < capacity_x) {
      state child = (state){capacity_x, top.y};
      if (parentOf.find(child) == parentOf.end()) {
        s.push(child);
        parentOf[child] = make_pair(top, 1);
      }
    }
    if (top.y < capacity_y) {
      state child = (state){top.x, capacity_y};
      if (parentOf.find(child) == parentOf.end()) {
        s.push(child);
        parentOf[child] = make_pair(top, 2);
      }
    }
    if (top.x > 0) {
      state child = (state){0, top.y};
      if (parentOf.find(child) == parentOf.end()) {
        s.push(child);
        parentOf[child] = make_pair(top, 3);
      }
    }
    if (top.y > 0) {
      state child = (state){top.x, 0};
      if (parentOf.find(child) == parentOf.end()) {

        s.push(child);
        parentOf[child] = make_pair(top, 4);
      }
    }
    if (top.y > 0) {
      state child = (state){min(top.x + top.y, capacity_x),
                            max(0, top.x + top.y - capacity_x)};
      if (parentOf.find(child) == parentOf.end()) {
        s.push(child);
        parentOf[child] = make_pair(top, 5);
      }
    }
    if (top.x > 0) {
      state child = (state){max(0, top.x + top.y - capacity_y),
                            min(top.x + top.y, capacity_y)};
      if (parentOf.find(child) == parentOf.end()) {
        s.push(child);
        parentOf[child] = make_pair(top, 6);
      }
    }
  }
  if (goal.x == -1 || goal.y == -1)
    return;
  path.push(make_pair(goal, 0));
  while (parentOf[path.top().first].second != 0)
    path.push(parentOf[path.top().first]);
}

int main() {
  stack<pair<state, int>> path;
  printf("Enter the capacities of the two jugs : ");
  scanf("%d %d", &capacity_x, &capacity_y);
  printf("Enter the target amount : ");
  scanf("%d", &target);
  dfs((state){0, 0}, path);
  if (path.empty())
    printf("\nTarget cannot be reached.\n");
  else {
    printf("\nNumber of moves to reach the target : %d\nOne path to the target "
           "is as follows:\n",
           path.size() - 1);
    while (!path.empty()) {
      state top = path.top().first;
      int rule = path.top().second;
      path.pop();
      switch (rule) {
      case 0:
        printf("State : (%d, %d)\n#\n", top.x, top.y);
        break;
      case 1:
        printf("State : (%d, %d)\nAction : Fill the first jug\n", top.x, top.y);
        break;
      case 2:
        printf("State : (%d, %d)\nAction : Fill the second jug\n", top.x,
               top.y);
        break;
      case 3:
        printf("State : (%d, %d)\nAction : Empty the first jug\n", top.x,
               top.y);
        break;
      case 4:
        printf("State : (%d, %d)\nAction : Empty the second jug\n", top.x,
               top.y);

        break;
      case 5:
        printf(
            "State : (%d, %d)\nAction : Pour from second jug into first jug\n",
            top.x, top.y);
        break;
      case 6:
        printf(
            "State : (%d, %d)\nAction : Pour from first jug into second jug\n",
            top.x, top.y);
        break;
      }
    }
  }
  return 0;
}