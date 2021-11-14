## RIVER SIZES

```

You are given a two-dimensional array of potentially unequal height and width.
It contains only 0s and 1s. This array represents a map: 0s are land, and 1s are water.
A "river" on this map consists of any number of contiguous, adjacent water squares,
where "adjacent" means "above", "below", "to the left of", or "to the right of"
(that is, diagonal squares are not adjacent).

Write a function which returns an array of the sizes of all rivers represented in the input matrix.
Note that these sizes do not need to be in any particular order.

For example:

const input = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
];

should return [1, 2, 2, 2, 5]

```
