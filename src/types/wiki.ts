export type WikiEntry = {
  id: string;
  data: { title: string };
  filePath: string;
};

export type TreeNode = {
  indexEntry: WikiEntry | null;
  pages: WikiEntry[];
  children: Map<string, TreeNode>;
};
