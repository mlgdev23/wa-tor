Initialize grid with water, fish, and sharks
Set initial parameters (e.g., fish and shark reproduction rates, energy levels, grid size)

While simulation is running:
    For each fish in the grid:
        Move fish to an adjacent empty cell randomly
        If fish moves, increment its age
        If fish can't move, increment its age, anyway
        If fish age >= reproduction age:
            Reproduce, placing a new fish in an adjacent empty cell
            Reset age to 0

    For each shark in the grid:
        List adjacent cells with fish
        If there are adjacent cells with fish:
            Choose a random cell with fish
            Move to the selected cell
            Consume the fish, increment the shark's energy
            Remove the consumed fish from the grid
        Else:
            Move shark to an adjacent cell randomly
            If shark moves, decrement its energy
            If shark's energy <= 0:
                Remove shark from the grid

        If shark energy >= reproduction energy:
            Reproduce, placing a new shark in an adjacent empty cell
            Reset energy to 0

    Update the grid for the next time step

    Render the grid (display fish, sharks, and empty cells)

    Pause for a short time (to control simulation speed)

End of simulation loop

In Creature model:
The all_creatures array will hold all the fish and sharks.  These objects have all the pertinent data, including location on the display grid

In Wator:
There is a grid 2-dimensional array that will identify each cell as a fish, shark, or ocean. Create a World class that will initialize this array with the empty ocean and populate it with the beginning number of fish and sharks, randomly.  The grid just holds 0, 1, or 2 in each located, and paints the corresponding color accordingly.

