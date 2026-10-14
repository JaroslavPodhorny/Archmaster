import { getJson } from '../../shared/http'
import type { ExamDetail, Index, PrincipleDetail, ReviewEntry, TaskDetail } from './types'

const BASE = '/api/exam-graph'

export function fetchIndex(signal?: AbortSignal): Promise<Index> {
  return getJson(BASE, signal)
}

export function fetchReview(signal?: AbortSignal): Promise<ReviewEntry[]> {
  return getJson(`${BASE}/review`, signal)
}

export function fetchTask(id: string, signal?: AbortSignal): Promise<TaskDetail> {
  return getJson(`${BASE}/tasks/${encodeURIComponent(id)}`, signal)
}

export function fetchPrinciple(id: string, signal?: AbortSignal): Promise<PrincipleDetail> {
  return getJson(`${BASE}/principles/${encodeURIComponent(id)}`, signal)
}

/** test as the address has it: 2025-B. */
export function fetchExam(test: string, signal?: AbortSignal): Promise<ExamDetail> {
  return getJson(`${BASE}/exam/${encodeURIComponent(test)}`, signal)
}
