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
