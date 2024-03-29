all
exclude_tag :whitespace
exclude_tag :line_length

exclude_rule 'MD024'
exclude_rule 'MD006' # Lists at beginning of line
rule 'MD007', :indent => 4 # List indentation
exclude_rule 'MD029' # Ordered List Item Prefix
exclude_rule 'MD033' # Inline HTML
exclude_rule 'MD034' # Bare URL used
exclude_rule 'MD040' # Fenced code blocks should have a language specified
exclude_rule 'MD041' # First line in file should be a top level header
