import { getJson } from '../../shared/http'
import type { TreeNode, TreeVersion } from './types'

export function fetchTree(version: TreeVersion, signal?: AbortSignal): Promise<TreeNode[]> {
  return getJson(version === 'new' ? '/api/topic-tree?tree=new' : '/api/topic-tree', signal)
}
