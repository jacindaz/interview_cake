# /foo
#   /bar
#   /baz
#     a.txt

# {/foo, /foo/bar, /foo/baz, /foo/baz/a.txt}
# get_subdirs(path) :: list of name

def list_child_dirs(root_path)
  case root_path
  when '/foo'
    ['bar', 'baz']
  when 'bar'
    []
  when 'baz'
    ['a.txt']
  else
    []
  end
end

# puts(list_child_dirs('/foo'))

def is_file?(string)
  # 'a.txt'
  # []
  # 'bar'

  if string.split('.')[1] == 'txt'
    true
  else
    false
  end
end

# puts(is_file?('a.txt'))
# puts(is_file?('/foo/bar/blah.txt'))

def get_full_paths(root_path, full_path, results)
  puts "\ntop of function root_path: #{root_path}, full_path: #{full_path}"

  # base case
  if is_file?(root_path)
    puts "is_file? results: #{results}"
  else
    puts "list_child_dirs: #{list_child_dirs(root_path)}, root_path: #{root_path}"
    list_child_dirs(root_path).each do |child_path|
      built_path = full_path + '/' + child_path
      puts "#{built_path}, full_path: #{full_path}, root_path: #{root_path}, child_path: #{child_path}"
      results << built_path
      puts "results: #{results}, child_path: #{child_path}"
      get_full_paths(child_path, built_path, results)
    end
  end

  results
end

get_full_paths('/foo', '/foo', [])
