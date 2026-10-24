import { getJson } from '../../shared/http'
import type { TreeNode } from './types'

export function fetchTree(signal?: AbortSignal): Promise<TreeNode[]> {
  return getJson('/api/topic-tree', signal)
}
