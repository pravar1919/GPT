'use client'

import ReactMarkdown from 'react-markdown'

export default function MatchResult({ result }: { result: { description: string; score: number } }) {
  return (
    <div className="max-w-3xl mx-auto bg-dark shadow p-6 rounded mt-8">
      <h2 className="text-2xl font-bold mb-4 text-center text-green-600">Resume Match Result</h2>

      <p className="text-lg font-semibold text-gray-700 mb-4 text-center">
        Match Score: <span className="text-blue-600">{result.score.toFixed(2)}%</span>
      </p>

      <div className="prose max-w-none">
        <ReactMarkdown>{result.description}</ReactMarkdown>
      </div>
    </div>
  )
}
